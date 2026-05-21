#!/bin/bash
printf "%-20s %-10s %-10s %-10s %-10s\n" "Archivo" "A" "T" "G" "C"
echo "------------------------------------------------------------"
for archivo in *.fasta; do
    if [ ! -f "$archivo" ]; then
        echo "No se encontraron archivos .fasta en el directorio"
        exit 1
    fi
    if [ ! -s "$archivo" ]; then
        continue
    fi
    A=$(grep -o -i 'A' "$archivo" | wc -l)
    T=$(grep -o -i 'T' "$archivo" | wc -l)
    G=$(grep -o -i 'G' "$archivo" | wc -l)
    C=$(grep -o -i 'C' "$archivo" | wc -l)
    printf "%-20s %-10s %-10s %-10s %-10s\n" "$archivo" "$A" "$T" "$G" "$C"
done