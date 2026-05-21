#!/bin/bash

read -p "Introduce tu masa en kg: " masa
read -p "Introduce tu altura en metros: " altura
imc=$(echo "scale=0; $masa / ($altura * $altura)" | bc)
echo "Tu índice de masa corporal (IMC) es: $imc"