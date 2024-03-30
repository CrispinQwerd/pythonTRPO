studentList = ["Вася", "Петя"]
gradesList = [5, 4]
while True:
    answer = int(input("выберите действие\n"
                       "1. Добавить студента\n"
                       "2. Удалить студента\n"
                       "3. Посмотреть весь список студентов и оценок\n"
                       "0. Выйти из программы\n"))
    if answer not in [1, 2, 3, 0]:
        print("Такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("Введите имя студента: ")
        newGrade = int(input("Введите оценку студента: "))
        studentList.append(newStudent)
        gradesList.append(newGrade)
    elif answer == 2:
        delStudent = input("Введите имя студента для удаления: ")
        if delStudent in studentList:
            index = studentList.index(delStudent)
            del studentList[index]
            del gradesList[index]
        else:
            print("Студент не найден")
    elif answer == 3:
        for student, grade in zip(studentList, gradesList):
            print(f"{student}: {grade}")
    elif answer == 0:
        break
