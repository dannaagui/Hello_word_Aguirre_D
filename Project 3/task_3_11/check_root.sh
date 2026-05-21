#!/bin/bash

check_root() {
    if [ $EUID -ne 0 ]; then
        echo "========================================="
        echo "WARNING: Insufficient permissions"
        echo "========================================="
        echo "This script must be run as root"
        echo "Your current UID is: $EUID (root has UID 0)"
        echo "Exiting script..."
        echo "========================================="
        exit 1
    fi
}

check_root
echo "✓ Script running as root successfully"