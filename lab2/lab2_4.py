import matplotlib.pyplot as plt

# Дано
N0 = 1000  # Общее количество изделий
failures_interval1 = 308  # Количество изделий, вышедших из строя за [0, 3000] часов
failures_interval2 = 25  # Количество изделий, вышедших из строя за [3000, 3100] часов

# 1. Вычисляем вероятность безотказной работы P(3100)
P_3100 = (N0 - (failures_interval1 + failures_interval2)) / N0

# 2. Вычисляем интенсивность отказов λ(3100)
# Интервал времени для второго интервала [3000, 3100] часов
t_2 = 3100
delta_t = 100
# Вычисляем интенсивность отказов
lambda_3100 = (failures_interval2 / delta_t) / (N0 - (failures_interval1 + failures_interval2))

# Визуализация
time = [0, 3100]
probability = [P_3100, P_3100]
intensity = [0, lambda_3100]

print("Вероятность безотказной работы (P(3100)): {:.4f}".format(P_3100))
print("Интенсивность отказов при t = 3100 часов (λ(3100)): {:.4f}".format(lambda_3100))

plt.figure(figsize=(10, 6))

# График вероятности безотказной работы
plt.plot(time, probability, label='P(t)', marker='o')

# График интенсивности отказов
plt.plot(time, intensity, label='λ(t)', marker='x')

plt.xlabel('Время (часы)')
plt.ylabel('Значение')
plt.title('Надежность и интенсивность отказов')
plt.legend()
plt.grid()

plt.show()
