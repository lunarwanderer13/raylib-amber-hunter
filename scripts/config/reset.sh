#!/bin/bash

CONFIG="$HOME/.config/AmberHunter/config.json"

if [ -f $CONFIG ]; then
    rm -- "$CONFIG"
    echo "Amber Hunter config reset."
else
    echo "Amber Hunter config not found."
fi

echo
