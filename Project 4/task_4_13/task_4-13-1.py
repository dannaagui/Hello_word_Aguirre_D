x = float(input("Введите число X: "))
y = float(input("Введите число Y: "))
z = float(input("Введите число Z: "))
w = float(input("Введите число W: "))

if x < y :
    min1 = x
else:
    min1 = y
if z < w:
    min2 = z
else:
    min2 = w
if min1 < min2:
    min = min1
else:
    min = min2
print(f"Минимальное число: {min}")