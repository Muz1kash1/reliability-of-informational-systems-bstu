import matplotlib.pyplot as plt
import numpy as np

# Дано
N0 = 1000  # Общее количество ламп
N_1000 = 75  # Число отказавших ламп за 1000 часов
N_2000 = 98  # Число отказавших ламп за 2000 часов
N_3000 = 115  # Число отказавших ламп за 3000 часов

# 1. Вычисляем вероятность безотказной работы P(3000)
P_3000 = (N0 - N_3000) / N0

# 2. Вычисляем вероятность отказа Q(3000)
Q_3000 = 1 - P_3000

# 3. Вычисляем интенсивность отказов λ(2000)
# Рассчитываем разницу между числом отказов за 2000 и 1000 часов
failures_2000_1000 = N_2000 - N_1000
# Вычисляем интенсивность отказов
lambda_2000 = failures_2000_1000 / (N0 - N_1000)

# Визуализация
time = [1000, 2000, 3000]
probability = [P_3000, P_3000, P_3000]
failure_probability = [Q_3000, Q_3000, Q_3000]
intensity = [0, lambda_2000, lambda_2000]

plt.figure(figsize=(10, 6))

# График вероятности безотказной работы
plt.plot(time, probability, label='P(t)', marker='o')

# График вероятности отказа
plt.plot(time, failure_probability, label='Q(t)', marker='x')

# График интенсивности отказов
plt.plot(time, intensity, label='λ(t)', marker='s')

plt.xlabel('Время (часы)')
plt.ylabel('Значение')
plt.title('Надежность и интенсивность отказов')
plt.legend()
plt.grid()

plt.show()
