### Задание 2

# Написать программу, которая:

# - Создает двумерную матрицу произвольного размера от 4 до 8 во высоте и ширине, заполненную значениями из списка **[-3, -5, -2, -12, 0, 15, 4, 7, 2]**

# - Выводит данную матрицу в форматированном виде. Пример:

# - Выводит сумму всех элементов отрицательных


import random # Импортируем модуль random для генерации случайных чисел

height = random.randint(4, 8) # Определяем случайную высоту матрицы от 4 до 8
width = random.randint(4, 8) # Определяем случайную ширину матрицы от 4 до 8

numbers = [-3, -5, -2, -12, 0, 15, 4, 7, 2] # Список возможных значений для заполнения матрицы

matrix = [] # Создаем пустой список для хранения строк матрицы

for i in range(height): # Генерируем строки матрицы ля каждой строки в диапазоне высоты матрицы

	row = [] # Создаем пустой список для новой строки

	for j in range(width):# Заполняем строку элементами для каждого элемента в строке (в пределах ширины)

		row.append(random.choice(numbers)) # Добавляем случайный элемент из списка numbers

	matrix.append(row)  # Добавляем сгенерированную строку в матрицу

summ = 0 # Инициализируем переменную для хранения суммы отрицательных чисел

for row in matrix: # Проходим по каждой строке матрицы

	for number in row: # Проходим по каждому элементу строки

		print(f"{number:4}", end=' ') # Выводим элемент с выравниванием по правому краю на 4 символа

		if number<0: # Если элемент отрицательный, добавляем его к сумме
			
			summ += number # добавление к сумме

	print()  # Переходим на новую строку после вывода всех элементов текущей строки

print(f"Сумма всех отрицательных элементов: {summ}")