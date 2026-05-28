import pandas as pd

df = pd.read_csv('wild_boars.csv')

median_values = df.median(numeric_only=True)

with open('median_values.txt', 'w') as f:
    for parameter, value in median_values.items():
        f.write(f"{parameter}: {value:.2f}\n")

print("Los valores medianos han sido guardados en 'median_values.txt'")

print("\nValores medianos:")
for parameter, value in median_values.items():
    print(f"{parameter}: {value:.2f}")