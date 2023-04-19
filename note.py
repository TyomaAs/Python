with open("26-File.txt", "w") as f:
    result = "Вивести прiзвище (перше слово поля Name) та рейтинги (поле Reyting) студентiв, рейтинги яких вiдрiзняються вiд середнього в межах 10:\n"
    for student in result:
        last_name = student.Name.split()[0]
        result += last_name + ": " + student.Rating + "\n"
    f.write(result)
    # відфільтрувати список студентів команди червоних
    red_team = filter(lambda student: student.Red, entryArray)
    result = "Вивести коди (поле Cod) та прiзвища студентiв команди червоних (iстинне поле Red) з використанням лямбда-виразiв:\n"
    for student in red_team:
        last_name = student.Name.split()[0]
        result += student.Cod + ": " + last_name + "\n"
    f.write(result)
    f.close()
