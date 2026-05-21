#!/bin/bash
if [ ! -f students.txt ]; then
    echo "Error: students.txt no encontrado"
    exit 1
fi
echo "========================================="
echo "        ESTADÍSTICAS DE NOTAS"
echo "========================================="
cat students.txt
echo "========================================="
suma=$(awk '{sum += $2} END {print sum}' students.txt)
echo "1. Suma total de evaluaciones: $suma"
promedio=$(awk '{sum += $2} END {printf "%.2f", sum/NR}' students.txt)
echo "2. Promedio de evaluaciones: $promedio"
max=$(awk 'NR==1{max=$2} $2>max{max=$2} END {print max}' students.txt)
echo "3. Calificación máxima: $max"
echo "========================================="