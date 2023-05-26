import math
from tkinter import *

root = Tk()

root['bg'] = '#AAAAAA'
root.title('Laboratory 3')
root.geometry('500x500')

root.resizable(width=False, height=False)

canvas = Canvas(root, width=500, height=500)
canvas.pack()


class Shape:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self, angle):
        self.angle += angle

    def __add__(self, other):
        return Trapezium(self.x + other.x, self.y + other.y, self.angle + other.angle, self.base1 + other.base1, self.base2 + other.base2, self.height + other.height)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.angle


class Trapezium(Shape):
    def __init__(self, x, y, angle, base1, base2, height):
        super().__init__(x, y, angle)
        self.base1 = base1
        self.base2 = base2
        self.height = height

    @property
    def area(self):
        return (self.base1 + self.base2) * self.height / 2

    # TODO: Fix incorrect angle calculation
    def rotated_vertices(self, angle):
        dx = (self.base2 / 2 - self.base1) / 2
        dy = self.height / 2
        r = math.sqrt(dx ** 2 + dy ** 2)
        phi = math.atan2(dy, dx) + math.radians(angle)
        x = self.x
        y = self.y

        vertices_old = [(-self.base1 / 2, -self.height / 2),
                        (self.base1 / 2, -self.height / 2),
                        (self.base2 / 2, self.height / 2),
                        (-self.base2 / 2, self.height / 2)]

        vertices = []
        for vertex in vertices_old:
            rotated_x = x + (vertex[0] * math.cos(phi) -
                             vertex[1] * math.sin(phi))
            rotated_y = y + (vertex[1] * math.cos(phi) +
                             vertex[0] * math.sin(phi))
            vertices.append((rotated_x, rotated_y))

        return vertices

    def show(self):
        canvas.delete("all")
        vertices = self.rotated_vertices(self.angle)
        vertices = [coord for vertex in vertices for coord in vertex]
        canvas.create_polygon(*vertices, fill="#ffa500", outline="#000000")


def main():
    # x = float(input("Введіть координату x: "))
    # y = float(input("Введіть координату y: "))
    # angle = float(input("Введіть кут повороту: "))
    # base1 = float(input("Введіть довжину першої основи: "))
    # base2 = float(input("Введіть довжину другої основи: "))
    # height = float(input("Введіть висоту: "))
    # trap = Trapezium(x, y, angle, base1, base2, height)
    trap = Trapezium(200, 200, 0, 200, 120, 80)
    trap.show()
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
            trap.show()
            print("Трапеція переміщена")
        elif choice == "2":
            angle = float(input("Введіть кут обертання (у градусах): "))
            trap.rotate(angle)
            trap.show()
            print("Трапеція обернута")
        elif choice == "3":
            print("Площа трапеції:", trap.area)
        elif choice == "4":
            vertices = trap.rotated_vertices(0)
            print("Координати вершин трапеції:")
            for vertex in vertices:
                print("({:.2f}, {:.2f})".format(vertex[0], vertex[1]))
        elif choice == "5":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == '__main__':
    main()
