#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script to get information from:
http://www.transtats.bts.gov/Data_Elements.aspx?Data=2
about carrier and airports
"""

from bs4 import BeautifulSoup
import requests
import urllib2



def extract_data(url, s):
    # Extract data from a html source from a URL
    r = s.get(url)
    soup = BeautifulSoup(r.text)
    data = {"eventvalidation": "",
            "viewstate": ""}

    eventvalidation_element = soup.find(id="__EVENTVALIDATION")
    data["eventvalidation"] = eventvalidation_element["value"]

    viewstate_element = soup.find(id="__VIEWSTATE")
    data["viewstate"] = viewstate_element["value"]

    return data




def make_request(data, s):
    # Make request to get data
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


def make_file(html):
    # Make file with the result data
    f = open("text.html", "w")
    f.write(html)


def options(soup, id):
    # Get data about options: airport and carriers
    option_values = []
    carrier_list = soup.find(id=id)
    for option in carrier_list.find_all('option'):
        option_values.append(option['value'])
    return option_values


def print_list(label, codes):
    # Print data
    print "\n%s:" % label
    for c in codes:
        print c


def get_web(url):
    # Get url
    page = urllib2.urlopen(url)
    page_source = page.read()
    return page_source

def main():
    # setup the location files
    URL = 'http://www.transtats.bts.gov/Data_Elements.aspx?Data=2'

    page_source = get_web(URL)
    soup = BeautifulSoup(page_source)

    codes = options(soup, "CarrierList")
    print_list("Carriers", codes)

    codes = options(soup, "AirportList")
    print_list("Airports", codes)

    s = requests.Session()
    data = extract_data(URL, s)

    html = make_request(data, s)

    make_file(html)

if __name__ == '__main__':
    main()
