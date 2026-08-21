#!/bin/bash

source "$(dirname "$0")/../path.sh"

if [ -f $DATA ]; then
    echo "Opened Amber Hunter data."
    nano -- $DATA
else
    echo "Amber Hunter data not found."
fi

echo
