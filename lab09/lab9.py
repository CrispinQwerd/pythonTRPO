studentList = ["Вася", "Петя"]
while True:
    answer = int(input("выберите действие\n"
                       "1. Добавить студента\n"
                       "2. Удалить студента\n"
                       "3. Посмотреть весь список студентов\n"
                       "0. Выйти из программы\n"))
    if answer not in [1, 2, 3, 0]:
        print("Такой команды нет")
        continue
    elif answer == 1:
        newStudent = input("Введите имя студента: ")
        studentList.append(newStudent)
    elif answer == 2:
        delStudent = input("Введите имя студента для удаления: ")
        if delStudent in studentList:
            studentList.remove(delStudent)
        else:
            print("Студент не найден")
    elif answer == 3:
        print(studentList)
    elif answer == 0:
        break
