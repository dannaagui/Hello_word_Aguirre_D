import pandas as pd

df = pd.read_csv('wild_boars.csv')

results = []

for column in df.columns:
    mode_values = df[column].mode()
    
    if len(mode_values) == 1:
        results.append(f"{column}: {mode_values.iloc[0]}")
    else:
        modes_str = ', '.join(str(val) for val in mode_values.values)
        results.append(f"{column}: {modes_str}")

with open('mode_values.txt', 'w', encoding='utf-8') as f:
    for line in results:
        f.write(line + '\n')

print("Модальные значения сохранены в файл 'mode_values.txt'")
for line in results:
    print(line)
    