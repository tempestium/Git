import time
import hashlib
import requests
import json

timestamp = str(time.time())
private_key = "VUL TUSSEN DEZE QUOTES JE EIGEN PRIVATE KEY IN!!"
public_key = "VUL TUSSEN DEZE QUOTES JE EIGEN PRIVATE KEY IN!!"

hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
md5digest = str(hash.hexdigest())
url = "http://gateway.marvel.com:80/v1/public/characters"
connection_url = url+"?ts="+timestamp+"&apikey="+public_key+"&hash="+md5digest
print(connection_url)
response = requests.get(connection_url)
jsontext = json.loads(response.text)

# om de JSON leesbaar te printen...
print(json.dumps(jsontext, sort_keys=True, indent=4))
print("\nGevonden characters in comics:")

# JSON-indeling kun je uit het geprinte resultaat halen of uit de Marvel docs!
for item in jsontext['data']['results'][0]['comics']['items']:
    print(item['name'])
print("\nGevonden characters in series:")

# JSON-indeling kun je uit het geprinte resultaat halen of uit de Marvel docs!
for item in jsontext['data']['results'][0]['series']['items']:
    print(item['name'])


# testing de mergedinggers
