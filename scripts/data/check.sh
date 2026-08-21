#!/bin/bash

source "$(dirname "$0")/../path.sh"

if [ -f $DATA ]; then
    echo "Amber Hunter data:"
    cat -- "$DATA"
else
    echo "Amber Hunter data not found."
fi

echo
