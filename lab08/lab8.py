import random
print("Добро пожаловать в игру камень ножницы бумага!")
playerScore = 0
botScore = 0

for i in range(3):
    answer = input("Что выберешь?\n").lower()

    if "камень" in answer:
        answer = "к"
    elif "ножницы" in answer:
        answer = "н"
    elif "бумага" in answer:
        answer = "б"
    else:
        print("Неправильный ввод. Попробуй еще раз.")
        continue

    botAnswer = random.choice(["камень", "ножницы", "бумага"])
    print(f"А я выберу {botAnswer}")
    botAnswer = botAnswer[0]

    if answer == botAnswer:
        print("Ничья!")
    elif (answer == "к" and botAnswer == "н") or \
         (answer == "н" and botAnswer == "б") or \
         (answer == "б" and botAnswer == "к"):
        print("Ты победил!")
        playerScore += 1
    else:
        print("Я победил!")
        botScore += 1

if playerScore == botScore:
    print("Ничья по итогам трех раундов!")
elif playerScore > botScore:
    print("Ты победил по итогам трех раундов!")
else:
    print("Я победил по итогам трех раундов!")
