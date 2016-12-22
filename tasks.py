# -*- coding: utf-8

import bitarray
import auxillary

import math
import random


def calculate_simple_reliability(elements, logical_structure_function):
    if not isinstance(elements, dict):
        return
    result = 0.0
    keys = elements.keys()
    count_of_elements = len(elements)
    for i in xrange(0, 2 ** count_of_elements):
        states_vector = bitarray.bitarray(auxillary.to_binary(i)[64 - count_of_elements:])
        table_of_states = {keys[j]: states_vector[j] for j in xrange(0, count_of_elements)}
        probability_of_state = auxillary.calculate_probability_of_system_state(table_of_states, elements)
        will_system_work = logical_structure_function(table_of_states)
        if will_system_work:
            result += probability_of_state

    return result


def calculate_reliability(elements, logical_structure_function):
    if not isinstance(elements, dict):
        return
    result = 0.0
    keys = elements.keys()
    count_of_elements = len(elements)

    # Для всех рабочих.
    states_vector = bitarray.bitarray(count_of_elements)
    states_vector.setall(True)
    table_of_states = {keys[j]: states_vector[j] for j in xrange(0, count_of_elements)}
    probability_of_state = auxillary.calculate_probability_of_system_state(table_of_states, elements)
    will_system_work = logical_structure_function(table_of_states)
    if will_system_work:
        result += probability_of_state

    # Для одного отказа.
    states_vector = bitarray.bitarray(count_of_elements)
    states_vector.setall(True)
    for i in xrange(0, count_of_elements):
        states_vector[i] = False  # Поставим один отказ.
        table_of_states = {keys[j]: states_vector[j] for j in xrange(0, count_of_elements)}
        probability_of_state = auxillary.calculate_probability_of_system_state(table_of_states, elements)
        will_system_work = logical_structure_function(table_of_states)
        if will_system_work:
            result += probability_of_state
        states_vector[i] = True  # Вернём как было.

    # Для двух отказов.
    states_vector = bitarray.bitarray(count_of_elements)
    states_vector.setall(True)
    for i in xrange(0, count_of_elements - 1):
        states_vector[i] = False
        for j in xrange(i + 1, count_of_elements):
            states_vector[j] = False
            table_of_states = {keys[j]: states_vector[j] for j in xrange(0, count_of_elements)}
            probability_of_state = auxillary.calculate_probability_of_system_state(table_of_states, elements)
            will_system_work = logical_structure_function(table_of_states)
            if will_system_work:
                result += probability_of_state
            states_vector[j] = True
        states_vector[i] = True

    # Для трёх отказов.
    count_of_vectors = math.factorial(count_of_elements) / math.factorial(3) / math.factorial(count_of_elements - 3)
    count_of_vectors //= 2
    states_vector = bitarray.bitarray(count_of_elements)
    states_vector.setall(True)
    bad_states = set()
    for vector_number in xrange(count_of_vectors):
        count_of_bad_states = len(bad_states)
        while len(bad_states) == count_of_bad_states:
            zero_positions = frozenset()
            while len(zero_positions) != 3:
                zero_positions = frozenset(
                    int(random.uniform(0, count_of_elements)) for i in xrange(0, 3)
                )
            bad_states.add(zero_positions)
        for zero_position in zero_positions:  # Сгенерировали 3 отказа.
            states_vector[zero_position] = False

        table_of_states = {keys[j]: states_vector[j] for j in xrange(0, count_of_elements)}
        probability_of_state = auxillary.calculate_probability_of_system_state(table_of_states, elements)
        will_system_work = logical_structure_function(table_of_states)
        if will_system_work:
            result += probability_of_state * 2

        for zero_position in zero_positions:  # Вернули как было.
            states_vector[zero_position] = True

    # Для четырёх отказов.
    count_of_vectors = math.factorial(count_of_elements) / math.factorial(4) / math.factorial(count_of_elements - 4)
    count_of_vectors //= 10
    states_vector = bitarray.bitarray(count_of_elements)
    states_vector.setall(True)
    bad_states = set()
    for vector_number in xrange(count_of_vectors):
        count_of_bad_states = len(bad_states)
        while len(bad_states) == count_of_bad_states:
            zero_positions = frozenset()
            while len(zero_positions) != 4:
                zero_positions = frozenset(
                    int(random.uniform(0, count_of_elements)) for i in xrange(0, 4)
                )
            bad_states.add(zero_positions)
        for zero_position in zero_positions:  # Сгенерировали 4 отказа.
            states_vector[zero_position] = False

        table_of_states = {keys[j]: states_vector[j] for j in xrange(0, count_of_elements)}
        probability_of_state = auxillary.calculate_probability_of_system_state(table_of_states, elements)
        will_system_work = logical_structure_function(table_of_states)
        if will_system_work:
            result += probability_of_state * 10

        for zero_position in zero_positions:  # Вернули как было.
            states_vector[zero_position] = True

    return result
