import matplotlib.pyplot as plt

# Данные
n_values = [18, 12, 9, 0, 3, 3]
time_intervals = [10, 20, 30, 40, 50, 60]  # Границы временных интервалов

# Вычисление среднего времени безотказной работы (T1)
N = sum(n_values)
T1 = sum([(time_intervals[i] * n_values[i]) for i in range(len(n_values))]) / N

# Вывод результатов
print("Среднее время безотказной работы (T1):", T1, "часов")

# Визуализация (гистограмма числа отказов)
plt.bar(time_intervals, n_values, width=10, align='center', label='Число отказов в интервале')
plt.xlabel('Временные интервалы (часы)')
plt.ylabel('Число отказов')
plt.title('Число отказов в разных временных интервалах')
plt.legend()
plt.grid()
plt.show()
