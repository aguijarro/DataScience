#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for
# your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the
# appropriate values in the data dictionary.
# All your changes should be in the 'extract_data' function
from bs4 import BeautifulSoup
import requests
import os
import json

# setup the location files
DATADIR = "../Data/"
DATAFILEOUT = "airport.html"
html_page = 'http://www.transtats.bts.gov/Data_Elements.aspx?Data=2'

# get data for web


def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}

    soup = BeautifulSoup(page, "lxml")
    ev = soup.find(id="__EVENTVALIDATION")
    data["eventvalidation"] = ev["value"]

    vs = soup.find(id="__VIEWSTATE")
    data["viewstate"] = vs["value"]

    return data

# post web page


def make_request(data, s):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = s.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
               data={'AirportList': "BOS",
                     'CarrierList': "VX",
                     'Submit': 'Submit',
                     "__EVENTTARGET": "",
                     "__EVENTARGUMENT": "",
                     "__EVENTVALIDATION": eventvalidation,
                     "__VIEWSTATE": viewstate
                     })

    return r.text


def test(webFile):
    s = requests.Session()
    r = s.get(html_page)
    data = extract_data(r.text)

    f = open(webFile, 'w')
    f.write(make_request(data, s))

    assert data["eventvalidation"] != ""
    assert data["eventvalidation"].startswith("/wEdAMUJQSsANZr")
    assert data["viewstate"].startswith("/wEPDwULLTE")

if __name__ == '__main__':
    webFile = os.path.join(DATADIR, DATAFILEOUT)
    test(webFile)
