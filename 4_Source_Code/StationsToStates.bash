#! /bin/bash

      STATION=""
      STATE=""
      COUNT=30568
      COUNTRY=""

      while read line; do
            STATION=`echo $line | cut -f1 -d "," | sed -e 's/\"/''/g'`
            STATE=`echo $line | cut -f6 -d "," | sed -e 's/\"/''/g'`
            COUNTRY=`echo $line | cut -f5 -d "," | sed -e 's/\"/''/g'`
            if [ $STATION -eq 999999 ]; then
                   STATION=`echo $line | cut -f2 -d "," | sed -e 's/\"/''/g'`
            fi
            if [ ! -z "$STATE" -a "$COUNTRY" == "US" ]; then
                   echo $STATION,$STATE >> stations.csv
            fi
            let "COUNT=$COUNT-1"
            echo $COUNT
            done < /mnt/data/ish-history.csv
