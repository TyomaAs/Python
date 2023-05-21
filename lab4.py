import tkinter as tk
from tkinter import messagebox, filedialog
from fractions import Fraction
import random


class RationalNumberGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Rational Number Generator")

        # create menu bar
        menubar = tk.Menu(self.master)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(
            label="Generate Random Rational Number", command=self.generate_number)
        file_menu.add_command(
            label="Read Rational Number from File", command=self.read_from_file)
        file_menu.add_separator()
        file_menu.add_command(
            label="Save Rational Number to File", command=self.save_to_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        self.master.config(menu=menubar)

        # create main window
        self.input_frame = tk.Frame(self.master)
        self.input_frame.pack(pady=20)

        self.number_label = tk.Label(
            self.input_frame, text="Rational Numbers:")
        self.number_label.pack(side=tk.LEFT, padx=10)

        self.number_entry = tk.Entry(
            self.input_frame, width=20, font=("Arial", 14))
        self.number_entry.pack(side=tk.LEFT)

        self.generate_button = tk.Button(
            self.input_frame, text="Generate Random Number", command=self.generate_number)
        self.generate_button.pack(side=tk.LEFT, padx=10)

        self.check_button = tk.Button(
            self.input_frame, text="Check Equality", command=self.check_equality)
        self.check_button.pack(side=tk.LEFT, padx=10)

        # create file menu buttons
        self.file_button_frame = tk.Frame(self.master)
        self.file_button_frame.pack(pady=10)

        self.save_button = tk.Button(
            self.file_button_frame, text="Save", command=self.save_to_file)
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.open_button = tk.Button(
            self.file_button_frame, text="Open", command=self.read_from_file)
        self.open_button.pack(side=tk.LEFT, padx=10)

    def generate_number(self):
        self.number_entry.delete(0, tk.END)
        fraction = Fraction(random.randint(0, 100), random.randint(1, 100))
        fraction2 = Fraction(random.randint(0, 100), random.randint(1, 100))
        self.number_entry.insert(0, str(fraction) + " " + str(fraction2))

    def read_from_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    number = file.readline().strip()
                    self.number_entry.delete(0, tk.END)
                    self.number_entry.insert(0, number)
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found.")

    def save_to_file(self):
        number = self.number_entry.get()
        if not number:
            messagebox.showerror("Error", "No number to save.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(number)
            except IOError:
                messagebox.showerror("Error", "Error writing to file.")

    def check_equality(self):
        number = self.number_entry.get()
        try:
            fr1 = ''
            fr2 = ''
            sec_i = 0
            for i in range(0, len((number))):
                if number[i] != ' ':
                    fr1 += number[i]
                else:
                    sec_i = i + 1
                    break
            for i in range(sec_i, len((number))):
                if number[i] != ' ':
                    fr2 += number[i]
                else:
                    sec_i = i
                    break
            num_1 = ['', '']
            num_2 = ['', '']
            j = 0
            for i in range(0, len((fr1))):
                if fr1[i] == '/':
                    j += 1
                else:
                    num_1[j] += fr1[i]
            j = 0
            for i in range(0, len((fr2))):
                if fr2[i] == '/':
                    j += 1
                else:
                    num_2[j] += fr2[i]
            if int(num_1[1]) == 0 or int(num_2[1]) == 0:
                messagebox.showerror("Error", "Cannot be divided by zero.")
            elif int(num_1[0]) / int(num_1[1]) == int(num_2[0]) / int(num_2[1]):
                messagebox.showinfo("Equality Check", "The numbers are equal.")
            else:
                messagebox.showinfo(
                    "Equality Check", "The numbers are not equal.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input.")


if __name__ == "__main__":
    root = tk.Tk()
    app = RationalNumberGUI(root)
    root.mainloop()
