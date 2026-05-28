import pandas as pd

df = pd.read_csv('wild_boars.csv')

average_values = df.mean(numeric_only=True)

with open('average_values.txt', 'w') as f:
    for parameter, value in average_values.items():
        f.write(f"{parameter}: {value:.2f}\n")

print("Los valores promedio han sido guardados en 'average_values.txt'")

print("\nValores promedio:")
for parameter, value in average_values.items():
    print(f"{parameter}: {value:.2f}")