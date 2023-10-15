a = list(map(int, input("Введите список чисел: ").split()))
b = a

maxPos = b.index(max(b))
minPos = b.index(min(b))

b[maxPos], b[minPos] = b[minPos], b[maxPos]
print(*b, sep = " ")