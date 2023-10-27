import random
import numpy as np
from scipy import stats
import math

# Ваши значения i, j и k
i = 1
j = 4
k = 5
num_simulations = 10000

def simulate_drunkard_behavior(i, j, k):
    current_state = 'B'  # Пьяница начинает на левой ноге
    transitions = 0

    while current_state not in ['D', 'E']:
        transitions += 1
        if current_state == 'B':
            next_state = random.choices(['A', 'D'], weights=[j/i+j, i/i+j])[0]
        elif current_state == 'A':
            next_state = random.choices(['A', 'B', 'C'], weights=[i/i+j+k, j/i+j+k, k/i+j+k])[0]
        elif current_state == 'C':
            next_state = random.choices(['A', 'E'], weights=[j/j+k, k/j+k])[0]
        current_state = next_state

    return transitions, current_state

total_transitions = 0
falls_in_river = 0

for _ in range(num_simulations):
    transitions, final_state = simulate_drunkard_behavior(i, j, k)
    total_transitions += transitions
    if final_state == 'D':
        falls_in_river += 1

average_transitions = total_transitions / num_simulations
observed_probability_falls_in_river = falls_in_river / num_simulations

# Теоретическая вероятность падения в реку
# Здесь вы можете использовать какую-либо статистику или теорию для расчета ожидаемой вероятности.

# Давайте предположим, что вы хотите сравнить наблюдаемую вероятность с 0.1 (10% вероятность).

expected_probability = 0.1

# Рассчитаем стандартную ошибку разности долей
se = math.sqrt((observed_probability_falls_in_river * (1 - observed_probability_falls_in_river) / num_simulations) + (expected_probability * (1 - expected_probability) / num_simulations))

# Рассчитаем Z-статистику
z = (observed_probability_falls_in_river - expected_probability) / se

# Вычислим двустороннее p-значение
p_value = 2 * (1 - abs(0.5 - 0.5 * math.erf(abs(z / math.sqrt(2)))))

print(f"Среднее время жизни пьяницы: {average_transitions:.2f} переходов")
print(f"Наблюдаемая вероятность упасть в реку: {observed_probability_falls_in_river:.4f}")
print(f"Теоретическая вероятность упасть в реку: {expected_probability:.4f}")
print(f"Z-статистика: {z:.4f}")
print(f"p-значение: {p_value:.4f}")

# Теперь вы можете проанализировать p-значение, чтобы сделать вывод о статистической значимости различия между наблюдаемой и ожидаемой вероятностями.