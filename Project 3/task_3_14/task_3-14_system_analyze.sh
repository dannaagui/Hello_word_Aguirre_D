#!/bin/bash
echo "========================================="
echo "     FILE SYSTEM USAGE ANALYSIS"
echo "========================================="
df -h | awk 'NR>1 {
    filesystem=$1
    use=$5
    gsub(/%/, "", use)
    printf "%-20s %s\n", filesystem, $5
    if (use > 90) {
        print "  ⚠ WARNING: File system " filesystem " is at " $5 " capacity!"
    }
}'