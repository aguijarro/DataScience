#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
import codecs
import json
from utils import update_data

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

CREATED = ["version", "changeset", "timestamp", "user", "uid"]
POS = ["lat", "lon"]

# return node_refs


def get_refs(element):
    refs = []
    for elem in element.iter("nd"):
        refs.append(elem.attrib['ref'])
    return refs


def get_created(element, node):
    created = {}
    lat = None
    lon = None

    for attrib in element.attrib:
        if attrib in CREATED:
                created[attrib] = element.attrib[attrib]
        elif attrib in POS:
            if attrib == 'lat':
                lat = element.attrib[attrib]
            else:
                lon = element.attrib[attrib]
        else:
            node[attrib] = element.attrib[attrib]

        if created:
            node['created'] = created
        if lat is not None and lon is not None:
            node['pos'] = [float(lat), float(lon)]
    return node


def get_address(element, node):
    address = {}
    # Build address move to function
    for elem in element.iter("tag"):
        if elem.attrib['k'].find('addr') != -1 and elem.attrib['k'].count(':') == 1:
            address[elem.attrib['k'].replace("addr:", "")] = elem.attrib['v']
        elif elem.attrib['k'].count(':') == 0:
            node[elem.attrib['k']] = elem.attrib['v']
        else:
            pass
    if address:
        if address.has_key('street'):
            address['street_better_name'] = update_data(address['street'])
        node['address'] = address
    return node


def shape_element(element):
    node = {}
    if element.tag == "node" or element.tag == "way":
        node['type'] = element.tag

        # Get node_refs
        node = get_created(element, node)

        node = get_address(element, node)

        # Get node_refs
        if element.tag == "way":
            node['node_refs'] = get_refs(element)
        return node
    else:
        return None


def process_map(file_in, pretty=False):
    # You do not need to change this file
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in ET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2) + "\n")
                else:
                    fo.write(json.dumps(el) + "\n")

