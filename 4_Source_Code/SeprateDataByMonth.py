#!/usr/bin/python                                                                                                              
import sys

def main(argv):
    for line in sys.stdin:
        month_temp=line.split()
        month=month_temp[0]
        if month[4:6] == "12" and int(month[0:4]) >= 2000:
            print line

if __name__ == "__main__":
    main(sys.argv)
