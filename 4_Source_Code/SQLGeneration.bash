#! /bin/bash                                                                                                                           

STATION=""
STATE=""

while read line; do
    STATION=`echo $line | cut -f1 -d ","`
    STATE=`echo $line | cut -f2 -d ","`
    echo "INSERT INTO US (SID, STATE) VALUES ($STATION, '$STATE');" >> sqlcommands
done < /root/stations.csv
