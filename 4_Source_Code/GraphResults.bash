#! /bin/bash

STATES_FILES=`ls data/`

for FILE  in $STATES_FILES; do

    clichart -c -d yyyyMM -l 0,1 --seriestitles "Temperature" -t  "$FILE Temperature" -y "Degrees F" -o "graphs/$FILE.png" "data/$FILE"

done
