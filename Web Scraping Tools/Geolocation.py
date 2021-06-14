from geopy.geocoders import Nominatim
import time
from pprint import pprint

# instantiate a new Nominatim client
app = Nominatim(user_agent="tutorial")

#get location raw data
location = app.geocode("Nairobi, Kenya").raw

pprint(location)

def get_location(address):
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return get_location(address)
    
address = "Makai Road, Masaki, Dar es Salaam, Tanzania"
location = get_location(address)
latitude = location["lat"]
longitude = location["lon"]
print(f"{latitude}, {longitude}")

pprint(location)
