files = ["seq1", "seq2.fasta", "seq3.fa", "seq4"]

date = "12.03.2026"

print(f"Дата взятия образца: {date}\n")

for name in files:
    if name.endswith((".fasta", ".fa")):
        print(f"{name} уже имеет расширение")
    else:
        new_name = name + ".fasta"
        print(f"{new_name} (расширение добавлено)")