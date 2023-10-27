import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Задаем параметр λ
# Замените это значение на номер по списку, разделенный на 4
list_number = 13  # Замените на свой номер
lambda_value = list_number / 4

# Генерируем 10000 чисел, имитирующих ξ
num_samples = 10000
samples = np.random.exponential(scale=1/lambda_value, size=num_samples)


# Вычисляем среднее значение выборки
sample_mean = np.mean(samples)

# Проверяем на уровне значимости 0,05
expected_mean = 1 / lambda_value
alpha = 0.05

z_score = (sample_mean - expected_mean) / (1 / np.sqrt(num_samples))

p_value = 2 * (1 - expon.cdf(z_score))  # Двусторонний тест

if p_value < alpha:
    print("Выборочное среднее не соответствует экспоненциальному распределению (p-значение =", p_value, ")")
else:
    print("Выборочное среднее соответствует экспоненциальному распределению (p-значение =", p_value, ")")

# Строим гистограмму частот
plt.hist(samples, bins=50, density=True, alpha=0.6, color='r', label='Гистограмма частот')
plt.xlabel('Значения случайной величины ξ')
plt.ylabel('Частота')
plt.legend()
plt.show()
