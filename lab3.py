import math

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
