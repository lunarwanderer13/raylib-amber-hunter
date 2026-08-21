#!/bin/bash

source "$(dirname "$0")/../path.sh"

if [ -f $CONFIG ]; then
    echo "Opened Amber Hunter config."
    nano -- $CONFIG
else
    echo "Amber Hunter config not found."
fi

echo
