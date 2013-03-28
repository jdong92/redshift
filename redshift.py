#https://code.google.com/p/geopy/wiki/GettingStarted

from subprocess import call
from geopy import geocoders

gn = geocoders.GoogleV3()

print "Please enter a zipcode: "
zipcode = raw_input()

out = gn.geocode(zipcode)

#Extract the longitude and latitude and split it into an array
lat = str(out[1]).split(",")

#Strip whitespaces and parenthesis
latitude = ((lat[0])[1:]).strip()
longitude = ((lat[1])[:-1]).strip()

call(["redshift", "-l", latitude+':'+longitude])
