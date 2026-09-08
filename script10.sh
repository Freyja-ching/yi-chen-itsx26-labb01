#!/bin/bash

# 1. Skapa mappar för varje filtyp (om de inte redan finns)
mkdir -p txt
mkdir -p pdf
mkdir -p jpg

# 2. Flytta filer till motsvarande mapp baserat på filändelse
mv *.txt txt/ 2>/dev/null
mv *.pdf pdf/ 2>/dev/null
mv *.jpg jpg/ 2>/dev/null

# 3. Logga händelsen med en tidsstämpel till loggfilen (Utmaning)
echo "$(date): Sorterade filer i mappen." >> organizer.log

echo "Sorteringen är klar!"