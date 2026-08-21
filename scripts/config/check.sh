#!/bin/bash

CONFIG="$HOME/.config/AmberHunter/config.json"

if [ -f $CONFIG ]; then
    echo "Amber Hunter config:"
    cat -- "$CONFIG"
else
    echo "Amber Hunter config not found."
fi

echo
