import math
import string
import fileinput


class person:
    id = 0
    payday1 = 0
    payday2 = 0
    name = "no name"
    edu = "no edu"
    profession = "no profession"
    yearOfBirth = "no year"


f_person = open('files\person.txt', "r")
f_payday = open('files\payday.txt', "r")

no_exit_program = False

while no_exit_program:
    print("1) Show person by ID:")
    print("2) Show persons by education:")
    print("3) Show persons by profession:")
    print("4) Show persons by the most popular profession:")
    print("5) Exit program:")
    choice = int(input("Enter the choice:\t"))
    switch(choice):
        case '1':
            a = 2


''' Завдання
Файл "Спiвробiтники" мiстить наступну iнформацiю про спiвробiтникiв: iндентифiкацiйний код, прiзвище та iнiцiали, вид освiти, фах, рiк народження. 

Файл "Зарплата" мiстить iндентифiкацiйний код, зарплату за перше пiврiччя, зарплату за друге пiврiччя. 

Розв’язати наступнi задачi:
a) Вивести прiзвища спiвробiтникiв з заданим видом освiти.
b) Вивести кiлькостi спiвробiтникiв, за кожним фахом.
c) Вивести зарплати спiвробiтникiв з найпопулярнiшим фахом.

Для обробки iнформацiї про спiвробiтника використовувати власний клас.'''
