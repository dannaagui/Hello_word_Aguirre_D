#!/bin/bash
cat > data.csv << 'EOF'
1,Mouse,23
2,Keyboard,15
3,Monitor,120
4,USB,5
EOF
echo "Archivo data.csv creado"
echo "========================================="
echo "1. Nombres de los productos:"
awk -F',' '{print "   " $2}' data.csv
echo "========================================="
echo "2. Productos con precio > 20:"
awk -F',' '$3 > 20 {print "   " $2 " - $" $3}' data.csv
echo "========================================="
total=$(awk -F',' '{sum += $3} END {print sum}' data.csv)
echo "3. Costo total: $" $total
echo "========================================="