#! /bin/bash

STATES=`ls data`

for STATE in $STATES; do
    cat data/$STATE | python process.py >> moredata/$STATE/12/data
done
