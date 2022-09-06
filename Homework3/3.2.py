a = int(input("Вес первого стула: "))
b = int(input("Вес второго стула: "))
c = int(input("Вес третьего стула: "))
d = int(input("Вес четвертого стула: "))

if a > b:
    if a > c:
        if a > d:
            print(1)
        else:
            print(4)
    else:
        if c > d:
            print(3)
        else:
            print(4)
else:
    if b > c:
        if b > d:
            print(2)
        else:
            print(4)
    else:
        if c > d:
            print(3)
        else:
            print(4)