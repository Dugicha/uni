from math import sin, cos, sqrt, atan2, radians

class City:
    def __init__(self, data = None):
        if data and data["location_type"] == "City":
            # Name
            self._name = data["title"]
            # Parse latitude and longitude
            lat, lng = data["latt_long"].split(",")
            self._lat = float(lat)
            self._lng = float(lng)
        else:
            print("Location must be a city!")

    @staticmethod
    def get_distance_between(city, other_city):
        lat1 = radians(city.latitude)
        lon1 = radians(city.longitude)
        lat2 = radians(other_city.latitude)
        lon2 = radians(other_city.longitude)
        R = 6373.0 # Radius of the Earth
        dlon = lon2 - lon1 # Difference in longitudes
        dlat = lat2 - lat1 # Difference in latitudes
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2 # Arc
        c = 2 * atan2(sqrt(a), sqrt(1 - a)) # Circumference of arc 'a'
        distance = R * c
        return distance

    @property
    def name(self):
        return self._name
    
    @property
    def latitude(self):
        return self._lat

    @property
    def longitude(self):
        return self._lng

    @name.setter
    def name(self, value):
        self._name = str(value)

    @latitude.setter
    def latitude(self, value):
        if isinstance(value, float):
            self._lat = value

    @longitude.setter
    def longitude(self, value):
        if isinstance(value, float):
            self._lng = value
