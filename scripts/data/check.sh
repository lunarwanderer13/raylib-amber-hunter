#!/bin/bash

DATA="$HOME/.local/share/AmberHunter/data.json"

if [ -f $DATA ]; then
    echo "Amber Hunter data:"
    cat -- "$DATA"
else
    echo "Amber Hunter data not found."
fi

echo
