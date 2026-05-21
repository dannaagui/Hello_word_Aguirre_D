#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Error: Faltan datos de entrada"
    exit 1
fi
echo "Expresión del gen $1 es de $2 unidades"