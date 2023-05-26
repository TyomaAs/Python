import tkinter as tk
from tkinter import messagebox, simpledialog


class Figura:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


class Circle(Figura):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def scale(self, coefficient):
        self.radius *= coefficient

    def get_touch_point(self):
        return self.x + self.radius, self.y


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Кола")
        self.geometry("400x300")

        self.canvas = tk.Canvas(self, width=400, height=300)
        self.canvas.pack()

        self.circle1 = None
        self.circle2 = None

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        task_menu = tk.Menu(menubar, tearoff=0)
        task_menu.add_command(
            label="Ввести координати та радіуси", command=self.enter_coordinates)
        task_menu.add_command(label="Масштабувати", command=self.scale_circle)
        menubar.add_cascade(label="Завдання", menu=task_menu)

    def enter_coordinates(self):
        x = simpledialog.askinteger(
            "Введення координат", "Введіть координату x:")
        y = simpledialog.askinteger(
            "Введення координат", "Введіть координату y:")
        radius = simpledialog.askinteger(
            "Введення радіусу", "Введіть радіус кола 1:")
        radius2 = simpledialog.askinteger(
            "Введення радіусу", "Введіть радіус кола 2:")
        self.circle1 = Circle(x - radius, y, radius)
        self.circle2 = Circle(x + radius2, y, radius2)
        self.draw_circles()

    def scale_circle(self):
        coefficient = simpledialog.askfloat(
            "Масштабування", "Введіть коефіцієнт масштабування:")
        if coefficient:
            self.circle1.scale(coefficient)
            self.circle2.scale(coefficient)
            self.circle1.move(-((self.circle1.radius *
                              coefficient) - self.circle1.radius)/coefficient, 0)
            self.circle2.move(
                ((self.circle2.radius * coefficient) - self.circle2.radius)/coefficient, 0)

            self.draw_circles()
        else:
            messagebox.showerror(
                "Помилка", "Введено некоректний коефіцієнт масштабування.")

    def draw_circles(self):
        self.canvas.delete("all")

        if self.circle1 and self.circle2:
            x1, y1, r1 = self.circle1.x, self.circle1.y, self.circle1.radius
            x2, y2, r2 = self.circle2.x, self.circle2.y, self.circle2.radius

            touch_point1 = self.circle1.get_touch_point()

            self.canvas.create_oval(
                x1 - r1, y1 - r1, x1 + r1, y1 + r1, outline="blue")
            self.canvas.create_oval(
                x2 - r2, y2 - r2, x2 + r2, y2 + r2, outline="red")

            self.canvas.create_oval(touch_point1[0] - 2, touch_point1[1] - 2, touch_point1[0] + 2,
                                    touch_point1[1] + 2, fill="black")


if __name__ == '__main__':
    app = Application()
    app.mainloop()
