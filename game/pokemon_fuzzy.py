import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

'''
Cria um sistema Fuzzy que recebe como input a diferença dos niveis
e o efeito do ataque e devolve como input a probabilidade de ganhar
'''
# Antecedents are the inputs of the rules
level = ctrl.Antecedent(np.arange(-9, 10, 1), 'level')
effect = ctrl.Antecedent(np.arange(0, 4.25, 0.25), 'effect')

# Consequents are the ouputs of the rules
probability = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'probability')

#Memberships Functions
level['weak'] = np.array([
    1.0, #-9
    1.0, #-8
    1.0, #-7
    0.8, #-6
    0.6, #-5
    0.4, #-4
    0.2, #-3
    0.0, #-2
    0.0, #-1
    0.0, # 0
    0.0, # 1
    0.0, # 2
    0.0, # 3
    0.0, # 4
    0.0, # 5
    0.0, # 6
    0.0, # 7
    0.0, # 8
    0.0  # 9

])
level['equal'] = np.array([
    0.0,  #-9
    0.0,  #-8
    0.0,  #-7
    0.0,  #-6
    0.0,  #-5
    0.0,  #-4
    0.2,  #-3
    0.5,  #-2
    0.8,  #-1
    1.0,  #0
    0.8,  #1
    0.5,  #2
    0.2,  #3
    0.0,  #4
    0.0,  #5
    0.0,  #6
    0.0,  #7
    0.0,  #8
    0.0   #9
])
level['strong'] = np.array([
    0.0,  # -9
    0.0,  # -8
    0.0,  # -7
    0.0,  # -6
    0.0,  # -5
    0.0,  # -4
    0.0,  # -3
    0.0,  # -2
    0.0,  # -1
    0.0,  # 0
    0.2,  # 1
    0.4,  # 2
    0.6,  # 3
    0.8,  # 4
    1.0,  # 5
    1.0,  # 6
    1.0,  # 7
    1.0,  # 8
    1.0  # 9
])

effect['immune'] = np.array([
    1.0,  # 0.00 → fully immune
    0.5,  # 0.25
    0.0,  # 0.50
    0.0,  # 0.75
    0.0,  # 1.00
    0.0,  # 1.25
    0.0,  # 1.50
    0.0,  # 1.75
    0.0,  # 2.00
    0.0,  # 2.25
    0.0,  # 2.50
    0.0,  # 2.75
    0.0,  # 3.00
    0.0,  # 3.25
    0.0,  # 3.50
    0.0,  # 3.75
    0.0  # 4.00
])

effect['low'] = np.array([
    0.0,  # 0.00
    0.5,  # 0.25
    1.0,  # 0.50 → not very effective
    0.5,  # 0.75
    0.0,  # 1.00
    0.0,  # 1.25
    0.0,  # 1.50
    0.0,  # 1.75
    0.0,  # 2.00
    0.0,  # 2.25
    0.0,  # 2.50
    0.0,  # 2.75
    0.0,  # 3.00
    0.0,  # 3.25
    0.0,  # 3.50
    0.0,  # 3.75
    0.0  # 4.00
])

effect['normal'] = np.array([
    0.0,  # 0.00
    0.0,  # 0.25
    0.0,  # 0.50
    0.5,  # 0.75
    1.0,  # 1.00 → normal effectiveness
    0.5,  # 1.25
    0.0,  # 1.50
    0.0,  # 1.75
    0.0,  # 2.00
    0.0,  # 2.25
    0.0,  # 2.50
    0.0,  # 2.75
    0.0,  # 3.00
    0.0,  # 3.25
    0.0,  # 3.50
    0.0,  # 3.75
    0.0  # 4.00
])

effect['effective'] = np.array([
    0.0,  # 0.00
    0.0,  # 0.25
    0.0,  # 0.50
    0.0,  # 0.75
    0.0,  # 1.00
    0.0,  # 1.25
    0.0,  # 1.50
    0.0,  # 1.75
    1.0,  # 2.00 → super effective (single type)
    0.8,  # 2.25
    0.5,  # 2.50
    0.2,  # 2.75
    0.0,  # 3.00
    0.0,  # 3.25
    0.0,  # 3.50
    0.0,  # 3.75
    0.0  # 4.00
])

effect['super_effective'] = np.array([
    0.0,  # 0.00
    0.0,  # 0.25
    0.0,  # 0.50
    0.0,  # 0.75
    0.0,  # 1.00
    0.0,  # 1.25
    0.0,  # 1.50
    0.0,  # 1.75
    0.0,  # 2.00
    0.0,  # 2.25
    0.5,  # 2.50
    0.8,  # 2.75
    1.0,  # 3.00
    1.0,  # 3.25
    1.0,  # 3.50
    1.0,  # 3.75
    1.0  # 4.00
])
probability['low'] = np.array([
    1.0,  # 0.0
    1.0,  # 0.1
    0.8,  # 0.2
    0.5,  # 0.3
    0.2,  # 0.4
    0.0,  # 0.5
    0.0,  # 0.6
    0.0,  # 0.7
    0.0,  # 0.8
    0.0,  # 0.9
    0.0  # 1.0
])
probability['medium'] = np.array([
    0.0,  # 0.0
    0.0,  # 0.1
    0.2,  # 0.2
    0.5,  # 0.3
    0.8,  # 0.4
    1.0,  # 0.5
    0.8,  # 0.6
    0.5,  # 0.7
    0.2,  # 0.8
    0.0,  # 0.9
    0.0  # 1.0
])
probability['high'] = np.array([
    0.0,  # 0.0
    0.0,  # 0.1
    0.0,  # 0.2
    0.0,  # 0.3
    0.2,  # 0.4
    0.5,  # 0.5
    0.8,  # 0.6
    1.0,  # 0.7
    1.0,  # 0.8
    1.0,  # 0.9
    1.0  # 1.0
])

#Rules
#Level Weak
rule1 = ctrl.Rule(level['weak'] & effect['super_effective'], probability['medium'])
rule2 = ctrl.Rule(level['weak'] & effect['effective'], probability['medium'])
rule3 = ctrl.Rule(level['weak'] & effect['normal'], probability['low'])
rule4 = ctrl.Rule(level['weak'] & effect['low'], probability['low'])
rule5 = ctrl.Rule(level['weak'] & effect['immune'], probability['low'])
#Level equal
rule6 = ctrl.Rule(level['equal'] & effect['super_effective'], probability['high'])
rule7 = ctrl.Rule(level['equal'] & effect['effective'], probability['high'])
rule8 = ctrl.Rule(level['equal'] & effect['normal'], probability['medium'])
rule9 = ctrl.Rule(level['equal'] & effect['low'], probability['low'])
rule10 = ctrl.Rule(level['equal'] & effect['immune'], probability['low'])
#Level strong
rule11 = ctrl.Rule(level['strong'] & effect['super_effective'], probability['high'])
rule12 = ctrl.Rule(level['strong'] & effect['effective'], probability['high'])
rule13 = ctrl.Rule(level['strong'] & effect['normal'], probability['medium'])
rule14 = ctrl.Rule(level['strong'] & effect['low'], probability['medium'])
rule15 = ctrl.Rule(level['strong'] & effect['immune'], probability['low'])



def calculate_prob(level_input, effect_input):
    # Clamp inputs to valid universe ranges
    level_input = max(-9, min(9, level_input))
    effect_input = max(0, min(4.0, effect_input))

    l_pos = np.where(level.universe == level_input)[0][0]
    e_pos = np.where(effect.universe == effect_input)[0][0]

    l_weak = level['weak'].mf[l_pos]
    l_equal = level['equal'].mf[l_pos]
    l_strong = level['strong'].mf[l_pos]

    e_immune = effect['immune'].mf[e_pos]
    e_low = effect['low'].mf[e_pos]
    e_normal = effect['normal'].mf[e_pos]
    e_effective = effect['effective'].mf[e_pos]
    e_super_effective = effect['super_effective'].mf[e_pos]

    r1 = min(l_weak, e_super_effective)  # → medium
    r2 = min(l_weak, e_effective)  # → medium
    r3 = min(l_weak, e_normal)  # → low
    r4 = min(l_weak, e_low)  # → low
    r5 = min(l_weak, e_immune)  # → low
    r6 = min(l_equal, e_super_effective)  # → high
    r7 = min(l_equal, e_effective)  # → high
    r8 = min(l_equal, e_normal)  # → medium
    r9 = min(l_equal, e_low)  # → low
    r10 = min(l_equal, e_immune)  # → low
    r11 = min(l_strong, e_super_effective)  # → high
    r12 = min(l_strong, e_effective)  # → high
    r13 = min(l_strong, e_normal)  # → medium
    r14 = min(l_strong, e_low)  # → medium
    r15 = min(l_strong, e_immune)  # → low

    high_r6 = np.minimum(r6, probability['high'].mf)
    high_r7 = np.minimum(r7, probability['high'].mf)
    high_r11 = np.minimum(r11, probability['high'].mf)
    high_r12 = np.minimum(r12, probability['high'].mf)

    med_r1 = np.minimum(r1, probability['medium'].mf)
    med_r2 = np.minimum(r2, probability['medium'].mf)
    med_r8 = np.minimum(r8, probability['medium'].mf)
    med_r13 = np.minimum(r13, probability['medium'].mf)
    med_r14 = np.minimum(r14, probability['medium'].mf)

    low_r3 = np.minimum(r3, probability['low'].mf)
    low_r4 = np.minimum(r4, probability['low'].mf)
    low_r5 = np.minimum(r5, probability['low'].mf)
    low_r9 = np.minimum(r9, probability['low'].mf)
    low_r10 = np.minimum(r10, probability['low'].mf)
    low_r15 = np.minimum(r15, probability['low'].mf)

    aggregated = np.maximum.reduce([
        high_r6, high_r7, high_r11, high_r12,
        med_r1, med_r2, med_r8, med_r13, med_r14,
        low_r3, low_r4, low_r5, low_r9, low_r10, low_r15
    ])

    result = fuzz.defuzz(
        probability.universe,
        aggregated,
        'centroid'
    )

    return result

    


