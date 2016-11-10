import time
import hashlib
import requests
import json
import csv
import random

def json2xml(json_obj, line_padding=""):
    result_list = list()

    json_obj_type = type(json_obj)

    if json_obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json2xml(sub_elem, line_padding))

        return "\n".join(result_list)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append("%s<%s>" % (line_padding, tag_name))
            result_list.append(json2xml(sub_obj, "\t" + line_padding))
            result_list.append("%s</%s>" % (line_padding, tag_name))

        return "\n".join(result_list)

    return "%s%s" % (line_padding, json_obj)

def create_marvel_xml():
    timestamp = str(time.time())
    private_key = "8da0333ed98c21b66ba3baf623b6105dd50dfdc7"
    public_key = "85838dc0baf3d8f1eb38ac2363afc12b"
    hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
    md5digest = str(hash.hexdigest())

    with open('helden_namen') as filecontent:
        filelines = filecontent.readlines()
        held = filelines[random.randrange(0,50)]
        held = held.replace('\n', '')
        print(held)

    url = "https://gateway.marvel.com:443/v1/public/characters?name=" + held

    connection_url = url+"&ts="+timestamp+"&apikey="+public_key+"&hash="+md5digest
    print(connection_url)
    response = requests.get(connection_url)
    s = json.loads(response.text)

    # om de JSON leesbaar te printen...
    #print(json.dumps(s, sort_keys=True, indent=4))

    # JSON-indeling kun je uit het geprinte resultaat halen of uit de Marvel docs!
    with open('marvel.json', 'w') as outfile:
        json.dump(s, outfile)
