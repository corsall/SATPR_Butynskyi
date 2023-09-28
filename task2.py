import numpy as np

ratings = np.array([
    [85, 30, 22, 0.65, 6],
    [60, 20, 10, 0.6, 7],
    [30, 12, 5, 0.45, 5],
    [75, 24, 13, 0.7, 8],
    [40, 15, 7, 0.55, 7]
])

weights = np.array([7, 5, 6, 8, 6])

# Знаходження мінімальних та максимальних значень по кожному стовпцю
mins = np.min(ratings, axis=0)
maxs = np.max(ratings, axis=0)

# Нормалізуємо всі значення
normalized_ratings = (ratings - mins) / (maxs - mins)

# Нормалізуємо значення ствопця 1 по спеціальній формулі
normalized_ratings[:, 1] = (maxs[1] - ratings[:, 1]) / (maxs[1] - mins[1])

print(normalized_ratings)

weighted_sums = np.sum(normalized_ratings * weights, axis=1)

position =  np.argmax(weighted_sums)

print(f"\nНайкраще обрати юриста: {position + 1} із функцією корисності: {weighted_sums[position]}")