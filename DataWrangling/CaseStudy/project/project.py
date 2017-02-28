# -*- coding: utf-8 -*-
import os
import pprint
from sample_file import make_file
from audit import audit, audit_city
from make_json import process_map
from analyze_data import draw_data

os.chdir('../data')
INPUT_FILE = "san-francisco-bay_california.osm"  # Replace this with your osm file
TEST_FILE = "sf_sample_sfb.osm"


def get_file_size(file):
    size = ((os.path.getsize(file)) / 1024) / 1024.0
    return size


def main():
    # Return original file size
    print("Original file size:", get_file_size(INPUT_FILE), "MB")
    # Make a sample file
    # make_file(INPUT_FILE, TEST_FILE)
    # Return sample file size
    print("Original file size:", get_file_size(TEST_FILE), "MB")
    # Audit addresses
    st_types, st_types_count = audit(TEST_FILE)
    # Audit city names
    city_types, city_types_count = audit_city(TEST_FILE)
    # Show data with errors
    print("** Audit Street **")
    pprint.pprint(dict(st_types))
    pprint.pprint(dict(st_types_count))

    print("** Audit Cities **")
    pprint.pprint(dict(city_types))
    pprint.pprint(dict(city_types_count))
    # Make JSON
    process_map(TEST_FILE, True)
    # Analyze data

    ##draw_data(dict(st_types_count), ("St", "Street"), (0, 0.15))
    ##draw_data(dict(st_types_count), ("Ave", "Ave.", "Avenue"), (0, 0, 0.15))
    ##draw_data(dict(st_types_count), ("Blvd", "Blvd.", "Boulevard"), (0, 0, 0.15))


if __name__ == '__main__':
    main()
