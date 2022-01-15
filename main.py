import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# 4 inputs
temperature = ctrl.Antecedent(np.arange(0, 11, 1), 'temperature')              # water temperature
hardness = ctrl.Antecedent(np.arange(0, 11, 1), 'hardness')                    # water hardness factor
softening_factor = ctrl.Antecedent(np.arange(0, 11, 1), 'softening_factor')    # washing powder softerning factor
user_duration = ctrl.Antecedent(np.arange(0, 11, 1), 'user_duration')          # user length duration

# 1 output
output1_duration = ctrl.Consequent(np.arange(0, 16, 1), 'duration')                 # output washing duration

temperature.automf(7)
hardness.automf(7)
softening_factor.automf(7)
user_duration.automf(7)

# define possible output states
output1_duration['lowest'] = fuzz.trimf(output1_duration.universe, [0, 0, 3])
output1_duration['lower'] = fuzz.trimf(output1_duration.universe, [0, 3, 5])
output1_duration['low'] = fuzz.trimf(output1_duration.universe, [3, 5, 8])
output1_duration['medium'] = fuzz.trimf(output1_duration.universe, [5, 8, 11])
output1_duration['high'] = fuzz.trimf(output1_duration.universe, [8, 11, 13])
output1_duration['higher'] = fuzz.trimf(output1_duration.universe, [11, 13, 15])
output1_duration['highest'] = fuzz.trimf(output1_duration.universe, [13, 15, 15])


# most pesimistic case 
r1 = ctrl.Rule(temperature['dismal'] | hardness['excellent'] | softening_factor['dismal'] | user_duration['excellent'], output1_duration['highest'])

# most optimistic case
r2 = ctrl.Rule(temperature['excellent'] | hardness['dismal'] | softening_factor['excellent'] | user_duration['dismal'], output1_duration['lowest'])

# medium cases
r3 = ctrl.Rule(temperature['dismal'] | hardness['poor'] | softening_factor['mediocre'] | user_duration['mediocre'], output1_duration['medium'])
r4 = ctrl.Rule(temperature['excellent'] | hardness['decent'] | softening_factor['decent'] | user_duration['excellent'], output1_duration['medium'])
r10 = ctrl.Rule(temperature['average'] | hardness['average'] | softening_factor['average'] | user_duration['average'], output1_duration['medium'])

r5 = ctrl.Rule(temperature['decent'] | hardness['mediocre'] | softening_factor['good'] | user_duration['mediocre'], output1_duration['lower'])
r6 = ctrl.Rule(temperature['average'] | hardness['good'] | softening_factor['average'] | user_duration['average'], output1_duration['medium'])
r7 = ctrl.Rule(temperature['poor'] | hardness['average'] | softening_factor['good'] | user_duration['average'], output1_duration['medium'])
r8 = ctrl.Rule(temperature['good'] | hardness['excellent'] | softening_factor['poor'] | user_duration['excellent'], output1_duration['high'])

r9 = ctrl.Rule(temperature['poor'] | hardness['mediocre'] | softening_factor['good'] | user_duration['average'], output1_duration['medium'])
r11 = ctrl.Rule(temperature['excellent'] | hardness['decent'] | softening_factor['good'] | user_duration['dismal'], output1_duration['lowest'])
r12 = ctrl.Rule(temperature['poor'] | hardness['mediocre'] | softening_factor['average'] | user_duration['poor'], output1_duration['higher'])
r13 = ctrl.Rule(temperature['excellent'] | hardness['good'] | softening_factor['decent'] | user_duration['mediocre'], output1_duration['low'])
r14 = ctrl.Rule(temperature['mediocre'] | hardness['dismal'] | softening_factor['average'] | user_duration['good'] , output1_duration['higher'])
r15 = ctrl.Rule(temperature['average'] | hardness['decent'] | softening_factor['excellent'] | user_duration['poor'], output1_duration['lower'])

# dismal
# poor
# mediocre
# average
# decent
# good
# excellent

# lowest
# lower
# low
# medium
# high
# higher
# highest

output_ctrl = ctrl.ControlSystem([r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15])
outputt = ctrl.ControlSystemSimulation(output_ctrl)


# Set up arguments
outputt.input['temperature'] = 1.0
outputt.input['hardness'] = 10.0
outputt.input['softening_factor'] = 1.0
outputt.input['user_duration'] = 10.0

outputt.compute()

print(outputt.output['duration'])
output1_duration.view(sim=outputt)
plt.show()

########

outputt.input['temperature'] = 10.0
outputt.input['hardness'] = 1.0
outputt.input['softening_factor'] = 10.0
outputt.input['user_duration'] = 1.0

outputt.compute()

print(outputt.output['duration'])
output1_duration.view(sim=outputt)
plt.show()

########

outputt.input['temperature'] = 5.0
outputt.input['hardness'] = 5.0
outputt.input['softening_factor'] = 5.0
outputt.input['user_duration'] = 5.0

outputt.compute()

print(outputt.output['duration'])
output1_duration.view(sim=outputt)
plt.show()

########

outputt.input['temperature'] = 3.1
outputt.input['hardness'] = 7.7
outputt.input['softening_factor'] = 1.0
outputt.input['user_duration'] = 3.2

outputt.compute()

print(outputt.output['duration'])
output1_duration.view(sim=outputt)
plt.show()

########

outputt.input['temperature'] = 4.4
outputt.input['hardness'] = 0.5
outputt.input['softening_factor'] = 9.2
outputt.input['user_duration'] = 5.2

outputt.compute()

print(outputt.output['duration'])
output1_duration.view(sim=outputt)
plt.show()
