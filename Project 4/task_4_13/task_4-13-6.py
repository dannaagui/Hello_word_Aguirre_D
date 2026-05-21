n = int(input("Введите числo N: "))

if n > 0: 
    s = 0
    for i in range(1, n + 1):
        s = s + i*i
    print("Сумма квадратов первых N чисел: ", s)