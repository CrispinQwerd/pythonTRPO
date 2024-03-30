import random

player_score = 0
bot_score = 0

def get_user_choice():
    while True:
        print("Выберите действие:")
        print("1. Камень")
        print("2. Ножницы")
        print("3. Бумага")
        choice = input("Введите число от 1 до 3: ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Неправильный ввод. Попробуйте снова.")

def get_bot_choice():
    return random.choice(["1", "2", "3"])

def get_choice_name(choice):
    if choice == "1":
        return "камень"
    elif choice == "2":
        return "ножницы"
    elif choice == "3":
        return "бумага"

def determine_winner(player_choice, bot_choice):
    if player_choice == bot_choice:
        return "Ничья!"
    elif (player_choice == "1" and bot_choice == "2") or \
         (player_choice == "2" and bot_choice == "3") or \
         (player_choice == "3" and bot_choice == "1"):
        return "Ты победил!"
    else:
        return "Я победил!"

print("Добро пожаловать в игру камень ножницы бумага!")

for _ in range(3):
    player_choice = get_user_choice()
    bot_choice = get_bot_choice()

    print(f"Ты выбрал {get_choice_name(player_choice)}, а я выберу {get_choice_name(bot_choice)}")

    result = determine_winner(player_choice, bot_choice)
    print(result)

    if "Я победил" in result:
        bot_score += 1
    elif "Ничья" in result:
        pass
    else:
        player_score += 1
    
    print("Робот: ", bot_score)
    print("Человек: ", player_score)

if player_score == bot_score:
    print("Ничья по итогам трех раундов!")
elif player_score > bot_score:
    print("Ты победил по итогам трех раундов!")
else:
    print("Я победил по итогам трех раундов!")
