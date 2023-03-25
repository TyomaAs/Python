import os
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
        print("ID:\t\t\t\t\t" + str(self.id))
        print("Name:\t\t\t\t\t" + self.name)
        print("Education:\t\t\t\t" + self.edu)
        print("Profession:\t\t\t\t" + self.profession)
        print("Year of born:\t\t\t\t" + str(self.year))
        print("Payday from first half of year:\t\t" + str(self.payday1) + "$")
        print("Payday from second half of year:\t" + str(self.payday2) + "$")

# * Start Program


file_person = open('files/persons.txt', "r")
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


no_exit_program = True

os.system("clear")

while no_exit_program:  # control menu
    print()
    print("1) Show person by ID:")
    print("2) Show persons by education:")
    print("3) Show persons by profession:")
    print("4) Show persons by the most popular profession:")
    print("5) Exit program:")
    print("0) Clear terminal :)")
    choice = int(input("\nEnter the choice: "))
    print()
    if choice == 1:
        id = int(input("Enter the ID: "))
        persons[id - 1].showInfo()
    if choice == 2:
        showByEducation(persons)
    elif choice == 5:
        no_exit_program = False
    elif choice == 0:
        os.system("clear")
print("\n\t\t\t\t\t\t\tThanks for using own my program and attention (^-^)\n")
