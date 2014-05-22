#! /bin/bash                                                                                      

STATES=`ls moredata/`

for STATE in $STATES; do
    MONTHS=`ls moredata/$STATE/`

    for MONTH in $MONTHS; do
        clichart -c -d yyyyMM -l 0,1 --seriestitles "Temperature" -t  "$STATE Temperature In $MON\
TH" -y "Degrees F" -o "moredata/$STATE/$MONTH/$MONTH.png" "moredata/$STATE/$MONTH/data"
    done

done
