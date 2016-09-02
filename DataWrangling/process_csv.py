# -*- coding: utf-8 -*-
'''
Transform csv files in dict structures and print in a pretty form
'''

import os
import pprint
import csv

# Set the directory for the data and the name of the file

DATADIR = '../Data/'
DATAFILE = 'beatles-diskography.csv'


def parse_csv(datafile):
    data = []
    # Open the file
    with open(datafile, 'rb') as sd:
        # Read data as a dictionary
        r = csv.DictReader(sd)
        for line in r:
            data.append(line)
    return data

if __name__ == '__main__':
    # get the file for work
    datafile = os.path.join(DATADIR, DATAFILE)
    # return a dict
    d = parse_csv(datafile)
    # print data
    pprint.pprint(d)
