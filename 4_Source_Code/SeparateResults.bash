#! /bin/bash

while read LINE; do

    STATE=`echo $LINE | cut -f1 -d " "`
    DATA=`echo $LINE | cut -f2 -d " "`
    DATA=$DATA","`echo $LINE | cut -f3 -d " "`
    echo $DATA >> "$STATE"

done < part-r-00000
