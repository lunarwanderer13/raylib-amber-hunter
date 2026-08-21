#!/bin/bash

DATA="$HOME/.local/share/AmberHunter"

if [ -f $DATA ]; then
    rm -- "$DATA"
    echo "Amber Hunter data reset."
else
    echo "Amber Hunter data not found."
fi

echo
