M = [1, 6, 9, 4, 7, 85]
n = len(M)

if n > 0 :
    sum = 0
    for i in range(n):
        if M[i] % 2 != 0 :
            sum = sum + M[i]
    print(f"Cумма всех нечетных элементов в массиве: {sum}")

else:
    print("Ошибка")