import random

botNumber = random.randint(1, 10)
playerNumber = int(input("Введите число: "))

while playerNumber != botNumber:
    if playerNumber > botNumber:
        print("Ты не угадал, моё число меньше твоего")
    else:
        print("Ты не угадал, моё число больше твоего")

    diff = abs(playerNumber - botNumber)
    if diff <= 2:
        print("Горячо!")
    elif diff <= 4:
        print("Тепло!")
    else:
        print("Холодно!")

    playerNumber = int(input("Введите число: "))

print(f"Ты угадал, моё число: {botNumber}")
