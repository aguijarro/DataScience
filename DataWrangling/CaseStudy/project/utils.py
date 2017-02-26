# UPDATE THIS VARIABLE
mapping = {"St": "Street",
           "St.": "Street",
           "Rd.": "Road",
           "Ave": "Avenue",
           "Ave.": "Avenue",
           "Blvd": "Boulevard",
           "Blvd.": "Boulevard",
           }


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
