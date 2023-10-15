a = list(map(int, input("Введите список чисел: ").split()))
b = []

for i in range(len(a)):
    b.append([])
    for j in range(len(a)):
        if a[j] > a[i]:
            b[i].append(a[j])

    if len(b[i]) > 0:
        print(f"Числа больше, чем {a[i]}: {', '.join(map(str, b[i]))}.")
    elif len(b[i]) == 0:
        print(f"Числа больше, чем {a[i]}: отсутствуют.")
    else:
        b.pop()