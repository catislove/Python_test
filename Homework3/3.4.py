a = str(input("Введите 3 первые цифры билета:"))
b = str(input("Введите 3 последние цифры билета: "))
x = int(a + b)

x1 = int(x / 100000)
x2 = int((float(x / 100000) - x1) * 10)
x3 = int((float(x / 10000) - int(x / 10000)) * 10)
x4 = int((float(x / 1000) - int(x / 1000)) * 10)
x5 = int((float(x / 100) - int(x / 100)) * 10)
x6 = int((float(x / 10) - int(x / 10)) * 10)

if (x1 + x2 + x3) == (x4 + x5 + x6):
    x = x + 1
    print(x)
else:
    print(x)
