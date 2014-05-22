#!/usr/bin/python                                                                                                                                                                                                                      

import sys
import boto

def main(argv):
    # GETS A DICTIONARY CONTAINING THE FILE STATIONS.CSV                                                                                                                                                                               
    s3 = boto.connect_s3('publicKeyGoesHere', 'privateKeyGoesHere')
    key = s3.get_bucket('tguthri1').get_key('stations.csv')
    b = key.get_contents_as_string()
    mapping = dict((int(n),v) for n,v in (a.split(',') for a in b.split()))

    # DICTIONARY TO HOLD STATE INDEXES                                                                                                                                                                                                 
    states = {
        "AK":0,
        "AL":1,
        "AR":2,
        "AZ":3,
        "CA":4,
        "CO":5,
        "CT":6,
        "DC":7,
        "DE":8,
        "FL":9,
        "GA":10,
        "HI":11,
        "IA":12,
        "ID":13,
        "IL":14,
        "IN":15,
        "KS":16,
        "KY":17,
        "LA":18,
        "MA":19,
        "MD":20,
        "ME":21,
        "MI":22,
        "MN":23,
        "MO":24,
        "MS":25,
        "MT":26,
        "NC":27,
        "ND":28,
        "NE":29,
        "NH":30,
        "NJ":31,
        "NM":32,
        "NV":33,
        "NY":34,
        "OH":35,
        "OK":36,
        "OR":37,
        "PA":38,
        "RI":39,
        "SC":40,
        "SD":41,
        "TN":42,
        "TX":43,
        "UT":44,
        "VA":45,
        "VT":46,
        "WA":47,
        "WI":48,
        "WV":49,
       "WY":50}

    # REVERSE LOOKUP FOR OUTPUT                                                                                                                                                                                                        
    reverse_states = dict((n,v) for v,n in states.iteritems())

    # CSV HEADER                                                                                                                                                                                                                       
    CSV = "State, January, February, March, April, May, June, July, August, September, October, November, December, Yearly Average \n"
    year_average = 0

    # ARRAYS/LISTS TO HOLD THE DATA (INITIALIZATION)                                                                                                                                                                                   
    averages = []
    totals = []
    counts = []
    for i in range(0,51):
       months1 = []
       months2 = []
       months3 = []
       for j in range(0,12):
           months1.append(0)
           months2.append(0)
           months3.append(0)
       averages.append(months1)
       totals.append(months2)
       counts.append(months3)

    # TRAVERSE THE INPUT FILE, GETTING THE MONTH, TEMPERATURE, STATION, STATE, AND YEAR                                                                                                                                                
    for line in sys.stdin:
        elements = line.split()

        if elements[2][4:6] != "MO":
            month = int(elements[2][4:6])
            year = int(elements[2][0:4])
            temp = float(elements[3])

           if elements[0] != "999999":
                station = elements[0]
            else:
                station = elements[1]
            state = mapping.get(int(station), 'NULL')

            if state != "NULL":
                state_index = states[state]
                # AVERAGE DATA STORAGE                                                                                                                                                                                                 
                totals[state_index][month - 1] = totals[state_index][month - 1] + temp
                counts[state_index][month - 1] = counts[state_index][month - 1] + 1

    # AVERAGE CALCULATIONS AND CSV CREATION                                                                                                                                                                                            
    for i in range(0, len(averages)):
        CSV = CSV + str(year) + ": " + str(reverse_states[i]) + ","
        for j in range (0,len(averages[i])):
            if counts[i][j] != 0:
                averages[i][j] = totals[i][j]/counts[i][j]
                CSV = CSV + str(averages[i][j])
                CSV = CSV + ","
                year_average = year_average + averages[i][j]
        year_average = year_average/12
        CSV = CSV + str(year_average)
        year_average = 0
        CSV = CSV + "\n"
    print CSV

if __name__ == "__main__":
    main(sys.argv)
