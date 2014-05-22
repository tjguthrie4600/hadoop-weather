#! /bin/bash      
for YEAR in {1929..2009}; do
    cat /mnt/gsod/$YEAR/* >> /mnt/gsod/$YEAR/$YEAR
    cat /mnt/gsod/$YEAR/$YEAR | grep -v YEARMODA >> /mnt/$YEAR
    sed -i 's/\( \)\{1,\}/,/g' /mnt/$YEAR
    s3cmd put FILE /mnt/$YEAR s3://tguthri1/Input/$YEAR
    rm /mnt/gsod/$YEAR/$YEAR /mnt/$YEAR
done
