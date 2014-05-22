#!/usr/bin/python                                                                                                              
import sys
import math

Xtotal = 0
count = 0
Ytotal = 0
XYtotal = 0
X2total = 0


# Traverse the input file
for line in sys.stdin:
    XY = line.split(',')
    if (len (XY) >= 2):

        X = float(XY[0])
        Y = float(XY[1])
    
        Xtotal = Xtotal + X
        Ytotal = Ytotal + Y
        XYtotal = XYtotal + X*Y
        X2total = X2total + pow(X,2)
        count = count + 1

if count != 0 and (count*X2total-pow(Xtotal,2) != 0):
    b=(count*XYtotal - Xtotal*Ytotal)/(count*X2total-pow(Xtotal,2)) 
    a=(Ytotal - b*Xtotal)/count       

    print "Y = " + str(b) + "X + " + str(a)
