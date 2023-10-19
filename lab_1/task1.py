import numpy as np

# Оцінки
ratings = np.array([
    [3, 7, 2, 9],
    [8, 3, 6, 7],
    [4, 8, 3, 5],
    [9, 6, 5, 4]
])

# Вага 
weights = np.array([8, 9, 6, 7])

# Розрахунок вагової суми для кожної альтернативи
# Відповідні значення перемножуються
# Потім значення сумуються за горизонталлю
weighted_sums = np.sum(ratings * weights, axis=1)

print(weighted_sums)

position =  np.argmax(weighted_sums)

print(f"\nНайкраще обрати адвоката: {position + 1} із функцією корисності: {weighted_sums[position]}")