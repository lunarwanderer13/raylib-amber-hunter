#!/bin/bash

source "$(dirname "$0")/../path.sh"

if [ -f $CONFIG ]; then
    echo "Amber Hunter config:"
    cat -- "$CONFIG"
else
    echo "Amber Hunter config not found."
fi

echo
