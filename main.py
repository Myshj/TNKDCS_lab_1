# -*- coding: utf-8

import data
import operability_functions
from ReliabilityCalculator import ReliabilityCalculator

# Надёжность напрямую без активной отказоустойчивости: 0.976312095712
# Надёжность по формуле без активной отказоустойчивости: 0.976310576399
# Надёжность по формуле с активной отказоустойчивостью: 0.983152593704

calculator = ReliabilityCalculator(data.elements, operability_functions.logical_structure_function, data.load_table)

#print(calculator.calculate_simple_reliability())
r = calculator.calculate_reliability(use_active_failover=True)
print r

c2 = ReliabilityCalculator(data.elements, operability_functions.logical_structure_function_1, data.load_table)
r = c2.calculate_reliability(use_active_failover=True)
print r