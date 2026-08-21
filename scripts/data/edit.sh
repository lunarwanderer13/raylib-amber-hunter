#!/bin/bash

DATA="$HOME/.local/share/AmberHunter/data.json"

if [ -f $DATA ]; then
    echo "Opened Amber Hunter data."
    nano -- $DATA
else
    echo "Amber Hunter data not found."
fi

echo
