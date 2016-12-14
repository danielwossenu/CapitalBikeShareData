import gmplot as gmp
import csv
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#This is a test for GITHUB

# read station coordinates into coor
data = csv.reader(open('stationCoordinates2.csv','rb'))
coor = []
for row in data:
    coor.append(row)

print coor

# split into intersection name, latitude, longitude and append to separate lists
# create dict object 'location' that a key of intersection names and values of [lat, longitude]
intersection = []
lat = []
lon = []
location = {}
for x in coor:
    if x[1] != 0:
        intersection.append(x[0])
        lat.append(float(x[1]))
        lon.append(float(x[2]))
        location[x[0]] = [float(x[1]), float(x[2])]
print lat
print lon

# read in all the trips for the quarter in pandas and split the start and end stations off to 'trips'
tripspd = pd.read_csv('C:/Users/Daniel/Desktop/Capital Bike Share Data/2016-Q3-Trips-History-Data-2.csv')
trips = tripspd[['Start station','End station']].values
print trips[0][0]

# create D.C. region map
gmap = gmp.GoogleMapPlotter(38.902652, -77.036593,12)

# plot stations on map
gmap.scatter(lat, lon, '#3B0B39', size=40, marker=False)
print location

# #plot trips
# for t in trips[:10000,:]:
#
#     # if t[1] == 'Woodmont Ave & Strathmore St':
#         loclats = [location[t[0]][0], location[t[1]][0]]
#         loclons = [location[t[0]][1], location[t[1]][1]]
#
#         if loclons[0] != 0 and loclons[1] !=0:
#             gmap.plot(loclats, loclons, 'cornflowerblue', edge_width=10)


# startstationsGPS = [[],[]]
# endstationsGPS = [[],[]]
# for t in trips[:10000,:]:
#     startstationsGPS[0].append(location[t[0]][0])
#     startstationsGPS[1].append(location[t[0]][1])
#     endstationsGPS[0].append(location[t[1]][0])
#     endstationsGPS[1].append(location[t[1]][1])
# gmap.heatmap(startstationsGPS[0],startstationsGPS[1], opacity=1.0)

cGPS = zip(lat,lon)
print cGPS

# # try a range of cluter numbers and print an elbow chart
# elbow = []
# for n in range(2,15):
#     cluster = KMeans(n_clusters=n).fit(cGPS)
#     elbow.append([n, cluster.inertia_])
# elbow = zip(*elbow)
# print elbow
# plt.plot(elbow[0],elbow[1])
# plt.show()

cluster = KMeans(n_clusters=8).fit(cGPS)
clusterpointdict = {}
for i,c in enumerate(cluster.cluster_centers_):
    clusterpointdict[i] = c

clusterpoints = cluster.predict(cGPS)
print clusterpoints

for each in zip(lat, lon, clusterpoints):
    center = clusterpointdict[each[2]]
    gmap.plot([each[0],center[0]], [each[1], center[1]], 'cornflowerblue', edge_width=5)



gmap.draw("myMap.html")