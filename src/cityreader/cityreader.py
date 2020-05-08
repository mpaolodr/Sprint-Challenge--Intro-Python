# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

# import CSV module
import csv


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lon = lon
        self.lat = lat

    def __str__(self):
        return f"{self.name}: ({self.lat}, {self.lon})"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list

    # I guess we could open this file without the csv module but just following instructions
    with open("cities.csv") as f:
        csv_reader = csv.reader(f)
        # I'll use this to skip the first line containing field names
        line = 0

        for row in csv_reader:
            # print(row)
            # each row is a list

            if line == 0:
                #   # do nothing and increment line to go to next line
                line += 1
            else:
                name = row[0]
                lat = float(row[3])
                lon = float(row[4])

                cities.append(City(name, lat, lon))

    return cities


cityreader(cities)


# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
lat1, lon1 = input("Enter values for lat1, lon1: ").split(",")
lat2, lon2 = input("Enter values for lat2, lon2: ").split(",")


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    # TODO Ensure that the lat and lon valuse are all floats
    c_lat1 = float(lat1)
    c_lat2 = float(lat2)
    c_lon1 = float(lon1)
    c_lon2 = float(lon2)

    # normalize values
    n_lat1 = None
    n_lat2 = None
    n_lon1 = None
    n_lon2 = None

    #  based on pattern, Lat1 and Lon1 are should always be greater than lat2 lon2
    # if lat1 and lon1 are less than lat2 and lon2 switch their values
    if c_lat1 > c_lat2:
        n_lat1 = c_lat1
        n_lat2 = c_lat2

        if c_lon1 > c_lon2:
            n_lon1 = c_lon1
            n_lon2 = c_lon2

        else:
            n_lon1 = c_lon2
            n_lon2 = c_lon1

    else:
        n_lat1 = c_lat2
        n_lat2 = c_lat1

        if c_lon1 > c_lon2:
            n_lon1 = c_lon1
            n_lon2 = c_lon2
        else:
            n_lon1 = c_lon2
            n_lon2 = c_lon1

    # check if values are normalized
    print(f"{n_lat1}, {n_lat2}, {n_lon1}, {n_lon2}")

    # Go through each city and check to see if it falls within
    # the specified coordinates.

    for city in cities:
        if(float(city.lat) <= n_lat1 and float(city.lat) >= n_lat2) and (float(city.lon) >= n_lon2 and float(city.lon) <= n_lon1):
            within.append(city)
        else:
            pass

    return within
