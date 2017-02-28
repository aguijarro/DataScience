# -*- coding: utf-8 -*-
# UPDATE THIS VARIABLE
mapping = {"St": "Street",
           "St.": "Street",
           "Rd.": "Road",
           "Ave": "Avenue",
           "Ave.": "Avenue",
           "Blvd": "Boulevard",
           "Blvd.": "Boulevard",
           }

# UPDATE THIS VARIABLE
mappingCities = {"jose": "Jose",
                 u'José': "Jose",
                 }


def updateCityName(name, mappingCities):
    for key, value in mappingCities.iteritems():
        find_name = name.find(key)
        if find_name != -1:
            new_name = name[find_name:]
            space_name = new_name.find(" ")
            if space_name != -1:
                pass
            else:
                if len(new_name) > len(key):
                    pass
                else:
                    name = name.replace(key, value)
                    break
    return name

def update_city(city):
    better_name = updateCityName(city, mappingCities)
    return better_name


def update_name(name, mapping):
    for key, value in mapping.iteritems():
        find_name = name.find(key)
        if find_name != -1:
            new_name = name[find_name:]
            space_name = new_name.find(" ")
            if space_name != -1:
                pass
            else:
                if len(new_name) > len(key):
                    pass
                else:
                    name = name.replace(key, value)
                    break
    return name


def update_data(address):
    better_name = update_name(address, mapping)
    return better_name
