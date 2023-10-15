a = list(map(int, input("Введите первый список чисел: ").split()))
b = list(map(int, input("Введите второй список чисел: ").split()))

print(f"Количество общих чисел: {len(list(set(a).intersection(b)))}")