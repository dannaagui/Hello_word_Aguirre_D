import pandas as pd
import numpy as np

df = pd.read_csv('wild_boars.csv')

with open('cv_tusks_by_sex.txt', 'w', encoding='utf-8') as f:
    for sexo in df['sex'].unique():
        df_sexo = df[df['sex'] == sexo]
        tusks_data = df_sexo['tusk_length_cm']
        
        media = tusks_data.mean()
        std = tusks_data.std()
        cv = (std / media) * 100 if media != 0 else np.nan
        
        f.write(f"{sexo}: {cv:.2f}%\n")
        print(f"{sexo}: {cv:.2f}%")

print("Результаты сохранены в 'cv_tusks_by_sex.txt'")