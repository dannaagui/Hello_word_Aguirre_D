import pandas as pd

df = pd.read_csv('wild_boars.csv')

columnas_para_analizar = [col for col in df.columns if col != 'weight_kg']

percentiles = [25, 50, 75, 90, 95]

with open('percentiles_output.txt', 'w', encoding='utf-8') as f:
    for columna in columnas_para_analizar:
        if pd.api.types.is_numeric_dtype(df[columna]):
            f.write(f"{columna}:\n")
            print(f"{columna}:")
            
            for p in percentiles:
                valor = df[columna].quantile(p / 100)
                if p == 25:
                    f.write(f"  Percentile {p} (Q1): {valor:.1f}\n")
                    print(f"  Percentile {p} (Q1): {valor:.1f}")
                elif p == 50:
                    f.write(f"  Median {p} (Q2): {valor:.1f}\n")
                    print(f"  Median {p} (Q2): {valor:.1f}")
                elif p == 75:
                    f.write(f"  Percentile {p} (Q3): {valor:.1f}\n")
                    print(f"  Percentile {p} (Q3): {valor:.1f}")
                else:
                    f.write(f"  Percentile {p}: {valor:.1f}\n")
                    print(f"  Percentile {p}: {valor:.1f}")
            
            max_val = df[columna].max()
            f.write(f"  Max: {max_val:.1f}\n\n")
            print(f"  Max: {max_val:.1f}\n")
            
            q1 = df[columna].quantile(0.25)
            q3 = df[columna].quantile(0.75)
            iqr = q3 - q1
            f.write(f"  IQR (Q3 - Q1): {iqr:.1f}\n\n")
            print(f"  IQR (Q3 - Q1): {iqr:.1f}\n")

print("\nResultados guardados en 'percentiles_output.txt'")