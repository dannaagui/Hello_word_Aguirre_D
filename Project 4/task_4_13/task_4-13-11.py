M = [3, 5, 75, 52, 34, 9]
n = len(M)

if n > 0 :
    sum = 0
    k = 0
    for i in range(n):
        if i % 2 == 0 :
            sum = sum + M[i]
            k = k + 1
    if k > 0 :
        av = sum / k
        print("Среднее арифметическое среди всех элементов с четными индексами: ", av)
    else:
        print("Ошибка")

else:
        print("Ошибка")