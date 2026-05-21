#!/bin/bash
if [ ! -f students.txt ]; then
    echo "Error: students.txt no encontrado"
    exit 1
fi
echo "=== ANÁLISIS DE ESTUDIANTES ==="
echo ""
echo "1. Estudiantes con nota > 80:"
awk '$2 > 80 {print "   " $1 " - " $2}' students.txt
echo ""
echo "2. Estudiantes con nota < 70:"
awk '$2 < 70 {print "   " $1 " - " $2}' students.txt
echo ""
echo "3. Primera línea del archivo:"
head -1 students.txt | awk '{print "   " $1 " - " $2}'