price = 0
mass = float(input("Введите вес конфет(в граммах): ")) 
if mass > 2000:
    mass = mass/1000
    price = 200
    result = price * mass
elif mass <=2000:
    mass = mass/1000
    price = 250
    result = price * mass
print(f"Масса конфет: {mass} кг")
print(f"Цена за кг: {price} рублей")
print(f"Вышло на: {result} рублей")
