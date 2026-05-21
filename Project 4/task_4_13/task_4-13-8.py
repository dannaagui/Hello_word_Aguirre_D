M = [3, -7, 45, -98, 2, 66]
n = len(M)
 
if n > 0 :
    k = 0
    for i in range(n) :
        if M[i] > 0 :
            k = k + 1
    print(f"Количество положительных чисел в массиве: {k}")

else:
    print("Ошибка")