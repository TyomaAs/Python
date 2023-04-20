import math
import os
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Базовий клас - фігура


class Shape:

    # Конструктор з координатами та кутом повороту
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    # Метод переміщення фігури на відстань dx, dy
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    # Метод повороту фігури на кут angle
    def rotate(self, angle):
        self.angle += angle

    # Операція додавання фігур
    def __add__(self, other):
        return Shape(self.x + other.x, self.y + other.y, self.angle + other.angle)

    # Ітератор для фігури, повертає координати та кут повороту
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.angle

# Похідний клас - трапеція


class Trapezium(Shape):
    # Конструктор з координатами, кутом повороту, довжинами основ та висотою
    def __init__(self, x, y, angle, base1, base2, height):
        super().__init__(x, y, angle)  # Виклик конструктора батьківського класу
        self.base1 = base1
        self.base2 = base2
        self.height = height

    # Властивість - обчислення площі трапеції
    @property
    def area(self):
        return (self.base1 + self.base2) * self.height / 2

    # Метод обчислення координат вершин трапеції після повороту на кут angle
    def rotated_vertices(self, angle):
        dx = self.base2 / 2 - self.base1 / 2
        dy = self.height / 2
        r = math.sqrt(dx ** 2 + dy ** 2)
        phi = math.atan2(dy, dx) + math.radians(angle)
        x = self.x + r * math.cos(phi)
        y = self.y + r * math.sin(phi)
        vertices = [(x - self.base1 / 2, y - self.height / 2),
                    (x + self.base1 / 2, y - self.height / 2),
                    (x + self.base2 / 2, y + self.height / 2),
                    (x - self.base2 / 2, y + self.height / 2)]
        return vertices


def main():
    os.system("clear")
    x = float(input("Введіть координату x: "))
    y = float(input("Введіть координату y: "))
    angle = float(input("Введіть кут повороту: "))
    base1 = float(input("Введіть довжину першої основи: "))
    base2 = float(input("Введіть довжину другої основи: "))
    height = float(input("Введіть висоту: "))
    trap = Trapezium(x, y, angle, base1, base2, height)

    print()
    while True:
        print("\n1. Перемістити трапецію")
        print("2. Обернути трапецію")
        print("3. Розрахувати площу трапеції")
        print("4. Вивести координати вершин трапеції")
        print("5. Вийти з програми")
        choice = input("Введіть номер опції: ")
        print()
        if choice == "1":
            dx = float(input("Введіть зміщення по осі x: "))
            dy = float(input("Введіть зміщення по осі y: "))
            trap.move(dx, dy)
            print("Трапеція переміщена")
        elif choice == "2":
            angle = float(input("Введіть кут обертання (у градусах): "))
            trap.rotate(angle)
            print("Трапеція обернута")
        elif choice == "3":
            print("Площа трапеції: ", trap.area)
        elif choice == "4":
            angle = float(input("Введіть кут повороту (у градусах): "))
            vertices = trap.rotated_vertices(angle)
            print("Координати вершин трапеції:")
            for vertex in vertices:
                print("({:.2f}, {:.2f})".format(vertex[0], vertex[1]))
        elif choice == "5":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


main()
