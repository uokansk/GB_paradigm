n = int(input("Введи число : "))

for i in range(1, n + 1):
    print(f"Таблица на {i}")
    for j in range(i, n + 1):
        print(f"{i} * {j} = {i * j}")
