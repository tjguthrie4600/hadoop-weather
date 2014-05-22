#! /bin/bash                                                                                                                    

      for YEAR in {1929..2009}
      do
        cat /mnt/data/gsod/$YEAR/* >> /mnt/data/gsod/$YEAR/$YEAR
        s3cmd put FILE /mnt/data/gsod/$YEAR/$YEAR s3://tguthri1
        rm /mnt/data/gsod/$YEAR/$YEAR
      done
