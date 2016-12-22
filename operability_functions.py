def f1(table_of_states):
    return \
        (table_of_states['pr1'] or table_of_states['pr2']) and \
        table_of_states['b1'] and \
        ((table_of_states['c1'] and (table_of_states['d1'] or table_of_states['d2'])) or
         (table_of_states['c2'] and (table_of_states['d2'] or table_of_states['d3'])))


def f2(table_of_states):
    return \
        (table_of_states['pr5'] or table_of_states['pr6']) and \
        table_of_states['b3'] and \
        table_of_states['c5'] and \
        (table_of_states['d7'] or table_of_states['d8'])


def f3(table_of_states):
    return \
        (table_of_states['pr4'] or table_of_states['pr5']) and \
        table_of_states['a1'] and \
        table_of_states['a3'] and \
        table_of_states['b1'] and \
        table_of_states['m2']


def f4(table_of_states):
    return \
        table_of_states['pr3'] and \
        table_of_states['b1'] and \
        table_of_states['a1'] and \
        table_of_states['m1'] and \
        table_of_states['c4'] and \
        table_of_states['d6']


def logical_structure_function(table_of_states):
    return f1(table_of_states) and f2(table_of_states) and f3(table_of_states) and f4(table_of_states)


# *********************************************************************************************************
def f1_1(table_of_states):
    return \
        (table_of_states['pr1'] or table_of_states['pr2']) and \
        table_of_states['b1'] and \
        ((table_of_states['c1'] and (table_of_states['d1'] or table_of_states['d2'] or table_of_states['d1_1'] or table_of_states['d2_1'])) or
         (table_of_states['c2'] and (table_of_states['d2'] or table_of_states['d3'] or table_of_states['d2_1'] or table_of_states['d3_1']))
         )


def f2_1(table_of_states):
    return \
        (table_of_states['pr5'] or table_of_states['pr6']) and \
        table_of_states['b3'] and \
        ((table_of_states['c5'] and (table_of_states['d7'] or table_of_states['d8'] or table_of_states['d7_1'] or table_of_states['d8_1']))
         )


def f3_1(table_of_states):
    return \
        (table_of_states['pr4'] or table_of_states['pr5']) and \
        table_of_states['a1'] and \
        table_of_states['a3'] and \
        table_of_states['b1'] and \
        table_of_states['m2']


def f4_1(table_of_states):
    return \
        table_of_states['pr3'] and \
        table_of_states['b1'] and \
        table_of_states['a1'] and \
        table_of_states['m1'] and \
        (table_of_states['c4'] and (table_of_states['d6'] or table_of_states['d6_1']))


def logical_structure_function_1(table_of_states):
    return f1_1(table_of_states) and f2_1(table_of_states) and f3_1(table_of_states) and f4_1(table_of_states)
