M = [1, 6, 9, 4, 7, 85]
n = len(M)

if n > 0 :
    sum = 0
    for i in range(n):
        if i % 2 != 0 :
            sum = sum + M[i]
    print(f"Cумма всех элементов в массиве с нечетными индексами: {sum}")

else:
    print("Ошибка")
    