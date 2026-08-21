#!/bin/bash

source "$(dirname "$0")/../path.sh"

if [ -f $DATA ]; then
    rm -- "$DATA"
    echo "Amber Hunter data reset."
else
    echo "Amber Hunter data not found."
fi

echo
