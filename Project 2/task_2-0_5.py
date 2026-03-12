name = "Данна"
group = "4731204/50001"
score = 5

print("Студент " + name + " из группы " + group + " получила " + str(score) + " баллов.")
f = open("result.txt", "w", encoding="utf-8")
print("Результаты работы", file=f)
f.close()