import pandas as pd
import numpy as np

df = pd.read_csv('wild_boars.csv')

with open('variance_std_cv.txt', 'w', encoding='utf-8') as f:
    for columna in df.columns:
        if pd.api.types.is_numeric_dtype(df[columna]):
            varianza = df[columna].var()
            std = df[columna].std()
            media = df[columna].mean()
            cv = (std / media) * 100 if media != 0 else np.nan
            
            f.write(f"{columna}:\n")
            f.write(f"  Дисперсия: {varianza:.2f}\n")
            f.write(f"  Стандартное отклонение: {std:.2f}\n")
            f.write(f"  Коэффициент вариации: {cv:.2f}%\n\n")
            
            print(f"{columna}:")
            print(f"  Дисперсия: {varianza:.2f}")
            print(f"  Стандартное отклонение: {std:.2f}")
            print(f"  Коэффициент вариации: {cv:.2f}%\n")

print("Результаты сохранены в 'variance_std_cv.txt'")