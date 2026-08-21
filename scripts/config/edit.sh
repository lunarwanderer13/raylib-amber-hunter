#!/bin/bash

CONFIG="$HOME/.config/AmberHunter/config.json"

if [ -f $CONFIG ]; then
    echo "Opened Amber Hunter config."
    nano -- $CONFIG
else
    echo "Amber Hunter config not found."
fi

echo
