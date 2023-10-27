import matplotlib.pyplot as plt

# Дано
N0 = 100  # Общее количество объектов
N_300 = 20  # Число отказавших объектов за 300 часов

# 1. Вычисляем вероятность безотказной работы P(300)
P_300 = (N0 - N_300) / N0

# 2. Вычисляем вероятность отказа Q(300)
Q_300 = 1 - P_300

# Визуализация
time = [300]
probability = [P_300]
failure_probability = [Q_300]

plt.figure(figsize=(8, 6))

# График вероятности безотказной работы
plt.plot(time, probability, label='P(t)', marker='o')

# График вероятности отказа
plt.plot(time, failure_probability, label='Q(t)', marker='x')

plt.xlabel('Время (часы)')
plt.ylabel('Значение')
plt.title('Надежность и интенсивность отказов')
plt.legend()
plt.grid()

plt.show()
