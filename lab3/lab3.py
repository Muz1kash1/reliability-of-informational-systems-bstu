import random
import numpy as np
import matplotlib.pyplot as plt

# Ваши значения i, j и k
i = 0.1
j = 0.4
k = 0.5
num_simulations = 10000

def simulate_mosquito_behavior(i, j, k):
    current_state = 'A'
    transitions = 0

    while True:
        if current_state == 'A':
            next_state = random.choices(['A', 'B', 'C'], weights=[1 - i - j, i, j])[0]
        elif current_state == 'B':
            next_state = random.choices(['A', 'B', 'C'], weights=[i, 1 - i - j, j])[0]
        elif current_state == 'C':
            next_state = random.choices(['A', 'B', 'C'], weights=[i, j, 1 - i - j])[0]
        
        transitions += 1
        if next_state == 'A':
            break  # Муха вернулась в A
        current_state = next_state

    return transitions

total_transitions = 0

for _ in range(num_simulations):
    total_transitions += simulate_mosquito_behavior(i, j, k)

average_transitions = total_transitions / num_simulations
print(f"Среднее количество переходов до первого возвращения в точку A: {average_transitions:.2f} секунд")