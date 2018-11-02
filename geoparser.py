import urllib
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(js, indent=4))

    #lat = js["results"][0]["geometry"]["location"]["lat"]
    #lng = js["results"][0]["geometry"]["location"]["lng"]
    #print('lat', lat, 'lng', lng)
    location = js['results'][0]['place_id']
    print('Place id: '+str(location))
text_file = open("Output.txt", "w")
text_file.write("Place ID: %s" % str(location))
text_file.close()
	