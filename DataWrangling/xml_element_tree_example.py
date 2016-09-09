import xml.etree.ElementTree as ET
import os

DATADIR = '../Data/'
DATAFILE = "exampleResearchArticle.xml"


def parseXml(dataFile):
    tree = ET.parse(dataFile)
    root = tree.getroot()
    return root

if __name__ == "__main__":
    dataFile = os.path.join(DATADIR, DATAFILE)
    root = parseXml(dataFile)
    for child in root:
        print child.tag

    # find one node
    title = root.find('./fm/bibl/title')

    title_text = ''
    for p in title:
        title_text += p.text

    print "\nTitle:\n", title_text

    # find all nodes

    print "\nEmails:\n"

    for a in root.findall('./fm/bibl/aug/au'):
        email = a.find('email')
        if email is not None:
            print email.text
