import math
import string
import fileinput

def showInfo(filePerson, filePay, id):
    person.id = id


def showID(filePerson, filePay, id):
    for i in filePerson:


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
    if choice == 1:
        id = int(input("Enter the ID: "))
        showID(id)
