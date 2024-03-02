counter = 0

answer = input("Столица России?\n")
if answer == "Москва" or answer == "москва":
    counter +=1
    print("Вы ответили верно")
else:
     print("Вы ответили не верно")
answer = input("Какой язык мы изучаем?\n")
if answer == "Python" or answer == "Пайтон":
    counter +=1
    print("Вы ответили верно")
else:
    print("Вы ответили не верно")
print (f"Вы набрали баллов {counter}")
   

    
   