#!/bin/bash

source "$(dirname "$0")/../path.sh"

if [ -f $CONFIG ]; then
    rm -- "$CONFIG"
    echo "Amber Hunter config reset."
else
    echo "Amber Hunter config not found."
fi

echo
