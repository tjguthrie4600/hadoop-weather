#! /bin/bash

while read line; do
    COUNT=`echo $line | cut -f1 -d "," | wc -m`
    if [ $COUNT == 7 ]; then
        station=`echo $line | cut -f1 -d ","`
        state=`echo $line | cut -f2 -d ","`
        output="$station,99999,$state"
        echo $output  >> US_STATIONS
    else
        echo 999999,$line >> US_STATIONS
    fi
done < stations.csv
