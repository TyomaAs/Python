import math # додавання бібліотеки

A = [1] # ініціалізація масиву
b = float(input("Введіть b:\t")) 
n = int(input("Введіть розмір масиву:\t"))
k = int(input("Введіть кількість виведення найменших елеменів:\t"))

c = math.sin(b) # обчислення другого елементу масиву
A.append(c) # додавання елементу до масиву
Overflow = False # булева змінна про введення k > n

if (k > n): # перевірка
    k = n # присвоєння виведення елементів рівної до кількості елементів масиву
    Overflow = True #* все ж k > n? ТАК

for i in range(3, n + 1): # заповнення масиву елементави за допомогою формули
    c += math.sin(b / (2 ** (i - 2))) # додавання до попереднього результату 
    A.append(c) # додавання елементу до масиву

A.sort() # сортування списку

for i in range(k): # виведення k елементів
    print(A[i]) # виведення

if (Overflow): # повідомлення при виведенні всіх елементів
    print("Виведено всі елементи списку") # виведення повідомлення