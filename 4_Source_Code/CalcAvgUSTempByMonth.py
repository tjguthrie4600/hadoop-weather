#!/usr/bin/python                                                                                                                                    
import sys

def main(argv):

    premonth="193610"
    total = 0
    count = 0
    avg = 0

    for line in sys.stdin:
        month_temp=line.split()
        month=month_temp[0]
        temp=month_temp[1]
       if premonth == month:
            total = total + float(temp)
            count = count + 1
        else:
            if count != 0:
                avg = total/count
            total = 0
            count = 0
            print str(month) + "," + str(avg)
        premonth = month

if __name__ == "__main__":
    main(sys.argv)