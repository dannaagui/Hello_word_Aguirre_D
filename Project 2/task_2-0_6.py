file_path = "output.txt"

with open(file_path, "w", encoding="utf-8") as f:
    print("Информация о студенте:", file=f)
    print("-" * 30, file=f)
    print("Имя: Данна", file=f)
    print("Фамилия: Агирре", file=f)
    print("Группа: 4731204/50001", file=f)
    print("Курс: 1", file=f)
    print("Год поступления: 2026", file=f)

print(f"Файл успешно создан: {file_path}")