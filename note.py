# import math  # це завдання 1

# a = float(input("Введіть a: "))
# b = float(input("Введіть b: "))

# if not a < 15:
#     a = math.sin(2 * a) + math.cos(2 * b)
# else:
#     a = math.sqrt(a + b ** 2)

# print("Результат: " + str(a))

# # =================================================================

# n = int(input("Введіть ціле число: "))  # це звадання 2
# result = 0

# for i in range(1, n + 1):
#     a = i + 1
#     result += a / i

# print("Результат обчислень: " + str(result))

# # =================================================================

# n = int(input("Введіть розмір масиву (списку): "))

# arr = []

# for i in range(0, n):
#     temp = float(input("Введіть елемент масиву (" + str(i) + "): "))
#     arr.append(temp)

# max_value = arr[0]
# max_index = 0
# sum = 0

# for i in range(1, n):
#     if max_value < arr[i]:
#         max_value = arr[i]
#         max_index = i
#     if i % 2 == 0:
#         sum += arr[i]


# print("Найбільший елемент масиву (його індекс " +
#       str(max_index) + "): " + str(max_value))
# print("Сума парних елементів масиву: " + str(sum))

# for i in range(n - 1, -1, -1):
#     if arr[i] < 0:
#         print(str(arr[i]) + "\t")
