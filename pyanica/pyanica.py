import random

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
probability_falls_in_river = falls_in_river / num_simulations

print(f"Среднее время жизни пьяницы: {average_transitions:.2f} переходов")
print(f"Вероятность упасть в реку: {probability_falls_in_river:.4f}")
