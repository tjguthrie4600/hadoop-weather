#!/usr/bin/python                                                                                                              
import sys

def main(argv):

    value=0  
    for line in sys.stdin:
        state_sno_fre=line.split()
        state=state_sno_fre[0]
        sno=state_sno_fre[1]
        freq=state_sno_fre[2]

        blue_sno=float(sno)
        
        if 1 > blue_sno > 0.5:
            value="E0E0E0"
        if 1.5 > blue_sno > 1:
            value="D8D8D8"
        if 2 > blue_sno > 1.5:
            value="D0D0D0"
        if 2.5 > blue_sno > 2:
            value="C8C8C8"
        if 3 > blue_sno > 2.5:
            value="C0C0C0"
        if 3.5 > blue_sno > 3:
            value="B8B8B8"
        if 4 > blue_sno > 3.5:
            value="B0B0B0" 
        if 4.5 > blue_sno > 4:
            value="A8A8A8"
        if 5 > blue_sno > 4.5:
            value="A0A0A0"
        if 5.5 > blue_sno > 5:
            value=989898
        if 6 > blue_sno > 5.5:
            value=909090
        if 6.5 > blue_sno > 6:
            value=888888
        if 7 > blue_sno > 6.5:
            value=808080
        if 7.5 > blue_sno > 7:
            value=787878
        if 8 > blue_sno > 7.5:
            value=707070
        if 8.5 > blue_sno > 8:
            value=686868
        if 9 > blue_sno > 8.5:
            value=606060
        if 9.5 > blue_sno > 9:
            value=585858
        if 10 > blue_sno > 9.5:
            value=505050
        if 10.5 > blue_sno > 10:
            value=484848
        if 11 > blue_sno > 10.5:
            value=404040
        if 11.5 > blue_sno > 11:
            value=383838
        if 12 > blue_sno > 11.5:
            value=303030
        if 12.5 > blue_sno > 12:
            value=282828
        if 13 > blue_sno > 12.5:
            value=202020
        if 13.5 > blue_sno > 13:
            value=181818
        print str(state) + " " + str(value)  
        

