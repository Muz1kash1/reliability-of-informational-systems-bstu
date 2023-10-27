import random
from scipy import stats
import matplotlib.pyplot as plt
# Задаем вероятности
i, j, k = 1 , 4, 5  # Замените на последние три цифры вашей зачетки
if i == 0:
    i = 10
if j == 0:
    j = 10
if k == 0:
    k = 10

total_probability = i/2 * (i + j + k) + (j + k)/2 * (i + j + k) + (i + k)/2 * (i + j + k) + j/2 * (i + j + k)

p0 = (i / 2 * (i + j + k)) / total_probability
p1 = ((j + k) / 2 * (i + j + k)) / total_probability
p2 = ((i + k) / 2 * (i + j + k)) / total_probability
p3 = (j / 2 * (i + j + k)) / total_probability

# Генерируем 10000 чисел, имитирующих ξ
num_samples = 10000
samples = [random.choices([0, 1, 2, 3], [p0, p1, p2, p3])[0] for _ in range(num_samples)]

# Считаем частоту появления каждого значения
count_0 = samples.count(0)
count_1 = samples.count(1)
count_2 = samples.count(2)
count_3 = samples.count(3)

# Выводим частоты
print("Частота 0:", count_0)
print("Частота 1:", count_1)
print("Частота 2:", count_2)
print("Частота 3:", count_3)

# Выполняем критерий сравнения долей


observed_frequencies = [count_0, count_1, count_2, count_3]
expected_frequencies = [num_samples * p0, num_samples * p1, num_samples * p2, num_samples * p3]

_, p_value = stats.chisquare(f_obs=observed_frequencies, f_exp=expected_frequencies)

# Проверяем на уровне значимости 0,05
alpha = 0.05
if p_value < alpha:
    print("Распределение не соответствует ξ (p-значение =", p_value, ")")
else:
    print("Распределение соответствует ξ (p-значение =", p_value, ")")

plt.bar([0, 1, 2, 3], observed_frequencies, tick_label=[0, 1, 2, 3])
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.title("Гистограмма частот")
plt.show()