

print("Сумма чётных чисел от 1 до 15")
print("-" * 35)

sum_even = 0

for i in range(1, 16):
    if i % 2 == 0:  # Проверка на чётность
        sum_even += i
        print(f"Добавлено {i}, текущая сумма: {sum_even}")

print("-" * 35)
print(f"Сумма всех чётных чисел от 1 до 15: {sum_even}") 