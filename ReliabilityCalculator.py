# -*- coding: utf-8

import bitarray
import auxillary
import math
import random


class ReliabilityCalculator(object):
    def __init__(self, elements, logical_structure_function, load_table):
        self._elements = elements
        self._logical_structure_function = logical_structure_function
        self._load_table = load_table
        self._statistics = None

    def calculate_simple_reliability(self):
        result = 0.0
        keys = self._elements.keys()
        count_of_elements = len(self._elements)
        for i in xrange(0, 2 ** count_of_elements):
            states_vector = bitarray.bitarray(auxillary.to_binary(i)[64 - count_of_elements:])
            table_of_states = {keys[j]: states_vector[j] for j in xrange(0, count_of_elements)}
            probability_of_state = auxillary.calculate_probability_of_system_state(table_of_states, self._elements)
            will_system_work = self._logical_structure_function(table_of_states)
            if will_system_work:
                result += probability_of_state

        return result

    def calculate_reliability_without_failures(self):
        """
        Вероятность того, что в системе не будет отказов.
        :return:
        """
        result = 0.0
        keys = self._elements.keys()
        count_of_elements = len(self._elements)

        states_vector = bitarray.bitarray(count_of_elements)
        states_vector.setall(True)
        table_of_states = {keys[j]: states_vector[j] for j in xrange(0, count_of_elements)}
        probability_of_state = auxillary.calculate_probability_of_system_state(table_of_states, self._elements)
        will_system_work = self._logical_structure_function(table_of_states)
        if will_system_work:
            result += probability_of_state

        return result

    def calculate_reliability_with_n_failures(self,
                                              count_of_failures,
                                              percent_of_possible_vectors_to_generate,
                                              use_active_failover
                                              ):
        """
        Вероятность того, что в системе случится ровно count_of_failures отказов, но она останется работоспособной.
        :param count_of_failures:
        :param percent_of_possible_vectors_to_generate:
        :return:
        """
        result = 0.0
        keys = self._elements.keys()
        count_of_elements = len(self._elements)

        count_of_vectors = math.factorial(count_of_elements) / math.factorial(count_of_failures) / math.factorial(
            count_of_elements - count_of_failures)
        count_of_vectors = int(count_of_vectors * percent_of_possible_vectors_to_generate)
        states_vector = bitarray.bitarray(count_of_elements)
        states_vector.setall(True)
        bad_states = set()
        for vector_number in xrange(count_of_vectors):
            zero_positions = self._add_new_bad_state(bad_states, count_of_failures, count_of_elements)
            auxillary.invert_at_positions(states_vector, zero_positions)

            table_of_states = {keys[j]: states_vector[j] for j in xrange(0, count_of_elements)}
            probability_of_state = auxillary.calculate_probability_of_system_state(table_of_states, self._elements)
            will_system_work = self._logical_structure_function(table_of_states) or \
                               (self.can_load_be_redistributed(table_of_states) and use_active_failover)
            if will_system_work:
                result += probability_of_state
            else:
                for key in table_of_states.keys():
                    if not table_of_states[key]:
                        self._statistics[key] += 1

            auxillary.invert_at_positions(states_vector, zero_positions)
        return result / percent_of_possible_vectors_to_generate

    def calculate_reliability(self, use_active_failover):
        self._statistics = {
            key: 0 for key in self._elements
            }
        return \
            self.calculate_reliability_without_failures() + self.calculate_reliability_with_n_failures(1, 1.0, use_active_failover) + \
            self.calculate_reliability_with_n_failures(2, 1.0, use_active_failover) + self.calculate_reliability_with_n_failures(3, 0.5, use_active_failover) + \
            self.calculate_reliability_with_n_failures(4, 0.1, use_active_failover)

    def can_load_be_redistributed(self, table_of_states):
        interesting_modules = {
            key for key in table_of_states.keys() if key in self._load_table.keys() and not table_of_states[key]
            }
        if len(interesting_modules) == 0:
            return False
        table_of_redistribution = {
            key: frozenset(
                redistribution_target for redistribution_target in self._load_table[key]['redistributions'] if
                redistribution_target not in interesting_modules
            ) for key in interesting_modules
            }
        # Вдруг для некоторых отказавших модулей вообще нельзя перераспределить нагрузку (отказали модули-дублёры)?
        if len(table_of_redistribution) != len(interesting_modules):
            return False
        # 0. Вдруг некоторые модули уже в номинале загружены так сильно, что их заменить никак нельзя?
        for key in table_of_redistribution.keys():
            if sum(
                    self._load_table[key]['redistributions'][target] for target in table_of_redistribution[key]
            ) < self._load_table[key]['nominal_load']:
                return False
        current_load = {
            key: self._load_table[key]['nominal_load'] for key in table_of_redistribution.keys()
            }
        # 1. Нагрузку с отказавших модулей сначала перераспределим на такие модули, которыми можно заменить только и только отказавший.
        unique_alternatives = {}
        for key in table_of_redistribution.keys():
            unique_alternatives[key] = table_of_redistribution[key]
            for temp_key in table_of_redistribution.keys():
                if temp_key != key:
                    unique_alternatives[key] -= table_of_redistribution[temp_key]
        for key in table_of_redistribution.keys():
            for target in unique_alternatives[key]:
                current_load[key] -= min(
                    self._load_table[target]['max_load'] - self._load_table[target]['nominal_load'],
                    self._load_table[key]['redistributions'][target])
        # 1.1 Может, этого хватило?
        if all(current_load[key] <= 0 for key in current_load.keys()):
            return True
        # 2. Теперь попытаемся распределить нагрузку на оставшиеся работоспособные модули.
        # 2.1. Забудем о тех, которых уже удовлетворили.
        for key in interesting_modules:
            if current_load[key] <= 0:
                current_load.pop(key, None)
                table_of_redistribution.pop(key, None)
        # 2.2. Если остался один неудовлетворённый, то и скатертью ему дорога (в пункте 0 проверили, что всё ОК).
        if len(current_load) <= 1:
            return True
        # 2.3. Подсчитаем, сколько у нас есть.
        current_possibilities = {}
        for key in self._load_table.keys():
            if key not in interesting_modules:
                current_possibilities[key] = self._load_table[key]['max_load'] - self._load_table[key]['nominal_load']
        for key in current_possibilities.keys():
            found = False
            for failed in current_load.keys():
                for target in table_of_redistribution[failed]:
                    if target == key:
                        found = True
            if not found:
                current_possibilities.pop(key, None)
        # 2.4. Может, у нас возможностей вообще меньше, чем желаний?
        if sum(current_load.values()) > sum(current_possibilities.values()):
            return False
        return True

    def _add_new_bad_state(self, bad_states, count_of_failures, count_of_elements):
        count_of_bad_states = len(bad_states)
        while len(bad_states) == count_of_bad_states:
            zero_positions = frozenset()
            while len(zero_positions) != count_of_failures:
                zero_positions = frozenset(
                    int(random.uniform(0, count_of_elements)) for i in xrange(0, count_of_failures)
                )
            bad_states.add(zero_positions)
        return zero_positions
