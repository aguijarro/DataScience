'''
Read xls or xlsx files to get the max, min, average, and date from one
column.

The script was developed by Udacity for Data Science Nanodegree.
'''

import xlrd
import os
import pprint

DATADIR = '../Data/'
DATAFILE = '2013_ERCOT_Hourly_Load_Data.xls'


def parse_xls(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = [[sheet.cell_value(r, col)
            for col in range(sheet.ncols)]
            for r in range(sheet.nrows)]

    cv = sheet.col_values(1, start_rowx=1, end_rowx=None)
    maxval = max(cv)
    minval = min(cv)

    maxpos = cv.index(maxval) + 1
    minpos = cv.index(minval) + 1

    maxtime = sheet.cell_value(maxpos, 0)
    realtime = xlrd.xldate_as_tuple(maxtime, 0)
    mintime = sheet.cell_value(minpos, 0)
    realmintime = xlrd.xldate_as_tuple(mintime, 0)

    dataRequiered = {'maxtime': realtime,
                     'maxvalue': maxval,
                     'mintime': realmintime,
                     'minvalue': minval,
                     'avgcoast': sum(cv) / float(len(cv))
                     }
    return dataRequiered

if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_xls(datafile)
    pprint.pprint(d)
