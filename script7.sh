#!/bin/bash

for file in *; do
    if [[ -f "$file" ]]; then
        echo "=== Fil: $file ==="
        cat "$file"
        echo ""
    fi
done