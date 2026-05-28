import pandas as pd

df = pd.read_csv('wild_boars.csv')

resultados = []

for sexo in df['sex'].unique():
    df_sexo = df[df['sex'] == sexo]
    
    q1 = df_sexo['length_cm'].quantile(0.25)
    q3 = df_sexo['length_cm'].quantile(0.75)
    iqr = q3 - q1
    
    resultados.append(f"{sexo}: Q1 = {q1:.1f} cm, Q3 = {q3:.1f} cm, IQR = {iqr:.1f} cm")

with open('iqr_by_sex.txt', 'w', encoding='utf-8') as f:
    for linea in resultados:
        f.write(linea + '\n')

print("Resultados guardados en 'iqr_by_sex.txt'")
for linea in resultados:
    print(linea)