sum = 0
counter = 0
number = int(input("Введите оценку от 1 до 12, 0 - прекратить ввод: "))
while number != 0:
    if 1 <= number <= 12:
        sum += number
        counter += 1
        number = int(input("Введите оценку от 1 до 12, 0 - прекратить ввод: "))
    else:
        print("Некорректная оценка. Пожалуйста, введите число от 1 до 12.")
        number = int(input("Введите оценку от 1 до 12, 0 - прекратить ввод: "))
if counter != 0:
    print("Средняя оценка:", sum / counter)
else:
    print("Оценок не было введено.")
