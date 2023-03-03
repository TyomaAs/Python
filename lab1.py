import math

size = int(input("Введіть кількість елементів масиву: "))
A = []

a = 1
b = 0

for i in range(size):  # * перелічуємо від i до кінця розміру масиву
    a *= (2 * (i + 1) - 1) * math.cos(i + 1)
    b += (i + 1) * (i + 1)
    A.append(a / b)

min = A[0]

for i in range(len(A)):
    for j in range(len(A)):
        if min < 0:
            minTemp = -min
        else:
            minTemp = min
        if A[j] < 0:
            ATemp = -A[j]
        else:
            ATemp = A[j]
        if minTemp > ATemp:
            min = A[j]
    #! B.append(min)
    print(min)
    A.remove(min)
    if len(A) != 0:
        min = A[0]
