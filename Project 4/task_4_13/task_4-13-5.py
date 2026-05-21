n = int(input("Введите числo N: "))

if n  > 0 :
    x = int(input("Введите первое числo : "))
    max = x
    for i in range(2, n + 1):
        y = int(input("Введите следующее число: "))
        if max < y :
            max = y
    print("Максимальное число: ", max)
elif n == 0 :
    print(0)
else:
    print("Ошибка")