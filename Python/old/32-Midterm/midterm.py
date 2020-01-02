import requests
from City import City

URL = "https://www.metaweather.com/api/location/search/?query="

def get_city_data(city_name):
    return requests.get(URL + city_name.strip().lower()).json()[0]

# Get data from API
d1 = get_city_data("paris")
d2 = get_city_data("vienna")
city1 = City(d1)
city2 = City(d2)

print(f"Distance between {city1.name} and {city2.name} is", 
    City.get_distance_between(city1, city2),"km")