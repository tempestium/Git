import time
import hashlib
import requests
import json
import csv

timestamp = str(time.time())
private_key = "8da0333ed98c21b66ba3baf623b6105dd50dfdc7"
public_key = "85838dc0baf3d8f1eb38ac2363afc12b"
hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
md5digest = str(hash.hexdigest())
url = "http://gateway.marvel.com:80/v1/public/characters?limit=100"

connection_url = url+"&ts="+timestamp+"&apikey="+public_key+"&hash="+md5digest
print(connection_url)
response = requests.get(connection_url)
s = json.loads(response.text)
# om de JSON leesbaar te printen...
print(json.dumps(s, sort_keys=True, indent=4))

# JSON-indeling kun je uit het geprinte resultaat halen of uit de Marvel docs!
#resultat=[]
w = csv.writer(open("output.csv", "w"))
for item in s['data']['results']:

    my_dict={}
    my_dict['name']=item.get('name')
    my_dict['description']=item.get('description')
    my_dict['thumbnail']=item.get('thumbnail').get('path')
    for sname in item['stories']['items']:
     my_dict['stories']=sname.get("name")
    for name in item['series']['items']:
     my_dict['series']=name.get('name')


    print(my_dict)
    #resultat.append(my_dict)

    for key, val in my_dict.items():
     w.writerow([key, val])
