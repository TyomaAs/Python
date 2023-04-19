import os
import math
import random
# * ^^^ Imports

# * Class and Functions


class person:
    id = 0
    payday1 = 0
    payday2 = 0
    name = "no name"
    edu = "no edu"
    profession = "no profession"
    year = "no year"

    def __init__(self, strInfo):
        string = ''
        i_temp = 0

        for i in range(i_temp, len(strInfo)):
            if strInfo[i] != '\t':
                string += strInfo[i]
            else:
                i_temp = i + 1
                break
        self.id = int(string)
        string = ""

        for i in range(i_temp, len(strInfo)):
            if strInfo[i] != '\t':
                string += strInfo[i]
            else:
                i_temp = i + 1
                break
        self.name = string
        string = ""

        for i in range(i_temp, len(strInfo)):
            if strInfo[i] != '\t':
                string += strInfo[i]
            else:
                i_temp = i + 1
                break
        self.edu = string
        string = ""

        for i in range(i_temp, len(strInfo)):
            if strInfo[i] != '\t':
                string += strInfo[i]
            else:
                i_temp = i + 1
                break
        self.profession = string
        string = ""

        for i in range(i_temp, len(strInfo)):
            if strInfo[i] != ';':
                string += strInfo[i]
            else:
                i_temp = i + 1
                break
        self.year = int(string)
        string = ""

        for i in range(i_temp, len(strInfo)):
            if strInfo[i] == '\t':
                i_temp = i + 1
                break

        for i in range(i_temp, len(strInfo)):
            if strInfo[i] != '\t':
                string += strInfo[i]
            else:
                i_temp = i + 1
                break
        self.payday1 = int(string)
        string = ""

        for i in range(i_temp, len(strInfo)):
            if strInfo[i] != ';':
                string += strInfo[i]
            else:
                break
        self.payday2 = int(string)

    def showInfo(self):
        print("\nID:\t\t\t\t\t" + str(self.id))
        print("Name:\t\t\t\t\t" + self.name)
        print("Education:\t\t\t\t" + self.edu)
        print("Profession:\t\t\t\t" + self.profession)
        print("Year of born:\t\t\t\t" + str(self.year))
        print("Payday from first half of year:\t\t" + str(self.payday1) + "$")
        print("Payday from second half of year:\t" + str(self.payday2) + "$\n")


def showHalfPersons(persons):
    half = math.ceil(len(persons)/2)  # half+ people
    showPersons = []
    i = 0
    while i < half:  # do while iteration < half people
        really = True
        a = int(random.randrange(1, len(persons) + 1))
        if len(showPersons) != 0:
            for j in range(0, len(showPersons)):  # check to equality id
                if persons[a - 1].name == showPersons[j]:
                    really = False
                    break
        if really:
            showPersons.append(str(persons[a - 1].name))
            i += 1
    i = 0
    for i in range(len(showPersons)):
        print(str(i + 1) + ") Name & first name: " + showPersons[i])


def showByEducation(persons, edu):
    counter = 0
    for i in range(0, len(persons)):
        if persons[i].edu == edu:
            persons[i].showInfo()
            counter += 1
    if counter != 0:
        print("\nPeople with " + edu + " are " + str(counter) + ".")
    else:
        print("\nNobody are with \"" + edu + "\" education.")


def ShowEducation_v2(persons):
    arr_edus = [persons[0].edu]
    arr_count = [1]
    for i in range(1, len(persons)):
        equals = False
        for j in range(0, len(arr_edus)):
            if persons[i].edu == arr_edus[j]:
                equals = True
                equals_count = j
                break
        if equals:
            arr_count[equals_count] += 1
        else:
            arr_edus.append(persons[i].edu)
            arr_count.append(1)
    for i in range(0, len(arr_edus)):
        print("Education \"" + arr_edus[i] + "\" are: " + str(arr_count[i]))


def showByMiddlePayday(persons):
    pay_Web = 0
    coun_Web = 0
    pay_Dev = 0
    coun_Dev = 0
    pay_Math = 0
    coun_Math = 0
    for i in range(len(persons)):
        if persons[i].profession == 'Web Developer':
            pay_Web += persons[i].payday1 + persons[i].payday2
            coun_Web += 2
        elif persons[i].profession == 'Developer':
            pay_Dev += persons[i].payday1 + persons[i].payday2
            coun_Dev += 2
        elif persons[i].profession == 'Mathematic':
            pay_Math += persons[i].payday1 + persons[i].payday2
            coun_Math += 2
    print('Middle payday for Web Developers = ' + str(pay_Web / coun_Web) + '$')
    print('Middle payday for Developers = ' + str(pay_Dev / coun_Dev) + '$')
    print('Middle payday for Mathematics = ' + str(pay_Math / coun_Math) + '$')


file_person = open('files/persons.txt', "r")  # * Start Program
file_payday = open('files/payday.txt', "r")

f_person = file_person.read()
f_payday = file_payday.read()

str_array = []
persons = []
str_temp = ''
j = 0

for i in range(0, len(f_person)):  # loop initialization strings
    if f_person[i] != '\n':
        str_temp += f_person[i]
    else:
        str_array.append(str_temp)
        str_temp = ''

for i in range(0, len(f_payday)):
    if f_payday[i] != '\n':
        str_temp += f_payday[i]
    else:
        str_array[j] += str_temp
        str_temp = ''
        persons.append(person(str_array[j]))  # initialize object class's
        j += 1


exit_program = False

os.system("clear")

while not exit_program:  # ! control menu
    print("\n1) Show person by ID:")
    print("2 a) Show persons by half random:")
    print("3 b) Show persons by education:")
    print("4 c) Show persons by middle value payday for all professions:")
    print("5 b) Show persons by education V2:")
    print("6) Exit program:")
    print("0) Clear terminal :)")
    choice = input("\nEnter the choice: ")
    print()

    if choice == '1':  # * Show person by ID
        id = int(input("Enter the ID: "))
        if id > 0 & id < len(persons):
            persons[id - 1].showInfo()
        else:
            print("You're enter unknown ID :(")

    elif choice == '2':  # * Show persons by half random
        showHalfPersons(persons)

    elif choice == '3':  # * Show persons by education
        edu = input("Enter the education: ")
        showByEducation(persons, edu)

    elif choice == '4':  # * Show persons by middle value payday for all professions
        showByMiddlePayday(persons)

    elif choice == '5':  # * Show persons by education v2
        ShowEducation_v2(persons)

    elif choice == '6':  # * Exit program
        exit_program = True

    elif choice == '0':  # * Clear terminal :)
        os.system("clear")

    else:
        print("You've enter uncorrect value :()")
print("\t\t\t\t\t\t\tThanks for using own my program and attention (^-^)\n")
