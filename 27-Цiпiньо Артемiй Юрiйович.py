
import os


class Human:
    def __init__(self, Name):
        self.Name = Name
        self.Rating = 0


class Student(Human):
    def __init__(self, Cod, Name, Red, Rating):
        super().__init__(Name)
        self.Cod = Cod
        self.Red = Red
        self.Rating = Rating


# Оголошення колекції студентів
students = [
    Student(Cod=12345, Name='Біркович Юрій Юрійович', Red=False, Rating=58),
    Student(Cod=12346, Name='Блага Денис', Red=False, Rating=36),
    Student(Cod=12347, Name='Богдан Олександра Степанівна',
            Red=False, Rating=54),
    Student(Cod=12348, Name='Вечей Максим Олександрович', Red=True, Rating=26),
    Student(Cod=12349, Name='Гироль Ігор Юрійович', Red=False, Rating=22),
    Student(Cod=12350, Name='Грабчак Даяна Олександрівна', Red=True, Rating=0),
    Student(Cod=12351, Name='Дівинець Антон Васильович', Red=False, Rating=47),
    Student(Cod=12352, Name='Калабухов Олександр Юрійович', Red=True, Rating=52),
    Student(Cod=12353, Name='Келарь Деніел Володимирович', Red=True, Rating=36),
    Student(Cod=12354, Name='Куруц Денис Вікторович', Red=True, Rating=8),
    Student(Cod=12355, Name='Логойда Віталій Олександрович',
            Red=False, Rating=48),
    Student(Cod=12356, Name='Мамчур Андрій Олегович', Red=True, Rating=58),
    Student(Cod=12357, Name='Мелеш Мирослав Мирославович', Red=True, Rating=14),
    Student(Cod=12358, Name='Мишустін Владислав Олексійович',
            Red=False, Rating=12),
    Student(Cod=12359, Name='Мондок Іван Іванович', Red=False, Rating=0),
    Student(Cod=12360, Name='Мощак Ростислав Юрійович', Red=False, Rating=58),
    Student(Cod=12361, Name='Носа Володимир Миколайович', Red=False, Rating=40),
    Student(Cod=12362, Name='Орел Володимир Юрійович', Red=False, Rating=57),
    Student(Cod=12363, Name='Павлик Даміан – Іван Володимирович',
            Red=True, Rating=58),
    Student(Cod=12364, Name='Путрашик Володимир Володимирович',
            Red=False, Rating=29),
    Student(Cod=12365, Name='Райхел Микола Юрійович', Red=True, Rating=10),
    Student(Cod=12366, Name='Рошко Іван Іванович', Red=False, Rating=34),
    Student(Cod=12367, Name='Савицька Анастасія Анатоліївна', Red=True, Rating=0),
    Student(Cod=12368, Name='Смолен Антон Олександрович', Red=False, Rating=58),
    Student(Cod=12369, Name='Степанов Денис Сергійович', Red=False, Rating=0),
    Student(Cod=12370, Name="Ценкнер Мар’ян Романович", Red=True, Rating=53),
    Student(Cod=12371, Name='Ціпіньо Артемій Юрійович', Red=False, Rating=60),
    Student(Cod=12372, Name='Шпринц Микола Миколайович', Red=False, Rating=30)
]

# Обчислення середнього рейтингу
total_reyting = sum(student.Rating for student in students)
average_reyting = total_reyting / len(students)


# Виведення імен та рейтингів студентів, чий рейтинг вище середнього
os.system('clear')
print("\nСтуденти з рейтингом вище середнього:")
for student in students:
    if student.Rating > average_reyting:
        last_name = student.Name.split()[0]
        print(last_name, student.Rating)


# Виведення імен та рейтингів студентів червоної команди, чий рейтинг нижче середнього по команді
print("\nСтуденти червоної команди з рейтингом нижче середнього:")
red_students = filter(lambda student: student.Red, students)
red_total_reyting = sum(student.Rating for student in red_students)
red_average_reyting = red_total_reyting / \
    len(list(filter(lambda student: student.Red, students)))
red_students = filter(
    lambda student: student.Red and student.Rating < red_average_reyting, students)
for student in red_students:
    last_name = student.Name.split()[0]
    print(last_name, student.Rating)


# Запис імен та рейтингів студентів у файл
f = open("27-File.txt", "w")
result = "Студенти з рейтингом вище середнього:\n"
for student in students:
    if student.Rating > average_reyting:
        last_name = student.Name.split()[0]
        result += last_name + '\t' + str(student.Rating) + '\n'
result += "\nСтуденти червоної команди з рейтингом нижче середнього:\n"
red_students = filter(
    lambda student: student.Red and student.Rating < red_average_reyting, students)
for student in red_students:
    last_name = student.Name.split()[0]
    result += last_name + '\t' + str(student.Rating) + '\n'
f.write(result)
f.close()
