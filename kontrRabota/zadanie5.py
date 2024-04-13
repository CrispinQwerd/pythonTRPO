import random
len = int(input("Введите длину пароля: "))

ranges = 10**(len-1)
rangee = (10**len) -1

print (random.randint(ranges,rangee))


