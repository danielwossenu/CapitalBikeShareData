import requests
import pandas as pd
import csv

#personal google maps geocoding api key, limited to 2500 requests per day
maps_api_key = 'AIzaSyBIOKU-c1rwEr_OHt1d1wWVvPOhOhYKFlM'

address = '18th St and Wyoming Ave NW, Washington DC'


def get_coordinates(intersection):
    intersection += ', Washington DC'
    intersection = intersection.replace("&",'and')
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+intersection+'&key='+maps_api_key)
    rj = response.json()
    if rj['status'] != 'OK':
        return 0, 0
    # print rj['status']
    latitude = rj['results'][0]['geometry']['location']['lat']
    longitude = rj['results'][0]['geometry']['location']['lng']

    return latitude, longitude

trips = pd.read_csv('C:/Users/Daniel/Desktop/Capital Bike Share Data/2016-Q3-Trips-History-Data-2.csv')
unique_stations = trips['Start station'].unique()
tripwriter = csv.writer(open('stationCoordinates.csv', 'w'), lineterminator = '\n')
for i, station in enumerate(unique_stations):
    lat, lng = get_coordinates(station)
    tripwriter.writerow([station, lat, lng])
    print i, '/403'


# print get_coordinates("3rd St and Pennsylvania Ave SE, Washington DC")
