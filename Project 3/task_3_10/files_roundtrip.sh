#!/bin/bash
echo "Creando archivos..."
for i in {1..10}; do
    touch "test$i.txt"
    echo "Creado: test$i.txt"
done
echo "------------------------"
echo "Eliminando archivos en orden inverso..."
contador=10
while [ $contador -ge 1 ]; do
    rm "test$contador.txt"
    echo "Eliminado: test$contador.txt"
    contador=$((contador - 1))
done
echo "------------------------"
echo "Proceso completado"