import bitarray
import math


def to_binary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(64)[::-1])


def invert_at_positions(vector, positions):
    for position in positions:
        vector[position] = not vector[position]


def calculate_probability_of_system_state(table_of_states, elements):
    result = 1
    for key in table_of_states.keys():
        if table_of_states[key]:
            result *= 1 - elements[key]['failure_probability']
        else:
            result *= elements[key]['failure_probability']

    return result
