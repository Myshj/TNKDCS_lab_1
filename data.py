elements = {
    'pr1': {
        'name': 'Pr1',
        'failure_probability': 6.2 * 10e-4
    },
    'pr2': {
        'name': 'Pr2',
        'failure_probability': 6.2 * 10e-4
    },
    'pr3': {
        'name': 'Pr3',
        'failure_probability': 6.2 * 10e-4
    },
    'pr4': {
        'name': 'Pr4',
        'failure_probability': 6.2 * 10e-4
    },
    'pr5': {
        'name': 'Pr5',
        'failure_probability': 6.2 * 10e-4
    },
    'pr6': {
        'name': 'Pr6',
        'failure_probability': 6.2 * 10e-4
    },
    'a1': {
        'name': 'A1',
        'failure_probability': 4.2 * 10e-4
    },
    'a3': {
        'name': 'A3',
        'failure_probability': 4.2 * 10e-4
    },
    'c1': {
        'name': 'C1',
        'failure_probability': 3.1 * 10e-4
    },
    'c2': {
        'name': 'C2',
        'failure_probability': 3.1 * 10e-4
    },
    'c4': {
        'name': 'C4',
        'failure_probability': 3.1 * 10e-4
    },
    'c5': {
        'name': 'C5',
        'failure_probability': 3.1 * 10e-4
    },
    'd1': {
        'name': 'D1',
        'failure_probability': 2.2 * 10e-5
    },
    'd2': {
        'name': 'D2',
        'failure_probability': 2.2 * 10e-5
    },
    'd3': {
        'name': 'D3',
        'failure_probability': 2.2 * 10e-5
    },
    'd6': {
        'name': 'D6',
        'failure_probability': 2.2 * 10e-5
    },
    'd7': {
        'name': 'D7',
        'failure_probability': 2.2 * 10e-5
    },
    'd8': {
        'name': 'D8',
        'failure_probability': 2.2 * 10e-5
    },
    'c1_1': {
        'name': 'C1',
        'failure_probability': 3.1 * 10e-4
    },
    'c2_1': {
        'name': 'C2',
        'failure_probability': 3.1 * 10e-4
    },
    'c4_1': {
        'name': 'C4',
        'failure_probability': 3.1 * 10e-4
    },
    'c5_1': {
        'name': 'C5',
        'failure_probability': 3.1 * 10e-4
    },
    'd1_1': {
        'name': 'D1',
        'failure_probability': 2.2 * 10e-5
    },
    'd2_1': {
        'name': 'D2',
        'failure_probability': 2.2 * 10e-5
    },
    'd3_1': {
        'name': 'D3',
        'failure_probability': 2.2 * 10e-5
    },
    'd6_1': {
        'name': 'D6',
        'failure_probability': 2.2 * 10e-5
    },
    'd7_1': {
        'name': 'D7',
        'failure_probability': 2.2 * 10e-5
    },
    'd8_1': {
        'name': 'D8',
        'failure_probability': 2.2 * 10e-5
    },
    'b1': {
        'name': 'B1',
        'failure_probability': 1.4 * 10e-5
    },
    'b3': {
        'name': 'B3',
        'failure_probability': 1.4 * 10e-5
    },
    'b4': {
        'name': 'B4',
        'failure_probability': 1.4 * 10e-5
    },
    'm1': {
        'name': 'M1',
        'failure_probability': 1.2 * 10e-4
    },
    'm2': {
        'name': 'M2',
        'failure_probability': 1.3 * 10e-4
    },
}

load_table = {
    'pr1': {
        'nominal_load': 40,
        'max_load': 100,
        'redistributions': {
            'pr2': 40,
            'pr3': 30,
            'pr4': 50
        }
    },
    'pr2': {
        'nominal_load': 50,
        'max_load': 120,
        'redistributions': {
            'pr1': 30,
            'pr3': 30,
            'pr4': 10,
            'pr5': 10
        }
    },
    'pr3': {
        'nominal_load': 50,
        'max_load': 100,
        'redistributions': {
            'pr1': 30,
            'pr2': 40,
            'pr4': 50,
            'pr5': 20
        }
    },
    'pr4': {
        'nominal_load': 30,
        'max_load': 90,
        'redistributions': {
            'pr1': 20,
            'pr2': 20,
            'pr3': 20,
            'pr5': 30
        }
    },
    'pr5': {
        'nominal_load': 70,
        'max_load': 150,
        'redistributions': {
            'pr1': 70,
            'pr2': 30,
            'pr4': 40
        }
    },
    'pr6': {
        'nominal_load': 50,
        'max_load': 100,
        'redistributions': {
            'pr7': 50
        }
    },
    'pr7': {
        'nominal_load': 50,
        'max_load': 100,
        'redistributions': {
            'pr6': 50
        }
    }
}