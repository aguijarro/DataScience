"""
Your task is to process the supplied file and
use the csv module to extract data from it.
The data comes from NREL (National Renewable
Energy Laboratory) website. Each file
contains information from one meteorological
 station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither
 data entry, nor header. It is a line
describing the data source. You should extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
You can use the csv modules "reader" method to get data in such format.
Another useful method is next() - to get the next line from the iterator.
You should only change the parse_file function.
"""

# Load libraries
import csv
import os

# setup the location files
DATADIR = "../../Data/"
DATAFILE = "745090.csv"


def parse_file(datafile):
    name = ""
    data = []
    # read file
    with open(datafile, 'rb') as f:

        reader = csv.reader(f, delimiter=',', quotechar='"')
        # get the first line to obtain the title
        title = f.readline().split(',')

        # get name
        name = title[1]
        name = name[1:len(name) - 1]

        # work with body data
        for row in reader:
            data.append(row)
        pass

    # Do not change the line below
    return (name, data)


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)

    # print results

    print name
    print data[0][1]
    print data[2][0]
    print data[2][5]

    # test data

    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()
