#! /bin/bash

STATES=`ls DATA_GRAPHS`

for STATE in $STATES; do
    MONTHS=`ls DATA_GRAPHS/$STATE | grep -v *.png | grep -v $STATE`
    for MONTH in $MONTHS; do
        cat DATA_GRAPHS/$STATE/$MONTH/data | python regress.py > DATA_GRAPHS/$STATE/$MONTH/regress_eq
    done
done