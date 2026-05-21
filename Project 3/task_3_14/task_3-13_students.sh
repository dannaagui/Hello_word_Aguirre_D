#!/bin/bash
cat > students.txt << 'EOF'
Ivan 78
Maria 92
Oleg 67
Anna 85
EOF
echo "Archivo students.txt creado"
echo "================================"
echo "1. Nombres de los estudiantes:"
awk '{print $1}' students.txt
echo "================================"
echo "2. Evaluaciones:"
awk '{print $2}' students.txt
echo "================================"
echo "3. Número de línea y nombre:"
awk '{print NR ". " $1}' students.txt
echo "================================"