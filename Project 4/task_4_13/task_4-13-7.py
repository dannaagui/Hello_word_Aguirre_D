M = [1, 5, 2, 8, 9]
n = len(M)

if n > 0 :
    sum = 0
    for i in range(n):
        sum = sum + M[i]
    av = sum / n
    print("Среднее арифметическое всех членов массива: ", av)

else:
    print("Ошибка")