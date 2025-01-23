import math
import argparse
'''
This uses the haversine formula to calculate the great-circle distance between two points –
that is, the shortest distance over the earth’s surface – giving an ‘as-the-crow-flies’ 
distance between the points (ignoring any hills they fly over, of course!).
source https://www.movable-type.co.uk/scripts/latlong.html
'''

def find_distance(lat_first, lon_first, lat_sec, lon_sec):

    R = 6371
    phi_first = math.radians(lat_first)
    phi_second = math.radians(lat_sec)
    diff_phi = math.radians(lat_sec - lat_first)
    diff_lambda = math.radians(lon_sec - lon_first)

    a = math.sin(diff_phi /2) ** 2 + math.cos(phi_first) * math.cos(phi_second) * math.sin(diff_lambda /2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d

'''
takes two arrays of locations as input
return the locations and and their shortes distances to another
'''

def find_shortest_distances(locs1, locs2):

    closest_locs = []
    for loc1 in locs1:
        lat_first, lon_first = loc1
        shortest_dist = float('inf')
        shortest_loc = None
        for loc2 in locs2:
            lat_second, lon_second = loc2
            curr_distance = find_distance(lat_first,lon_first,lat_second,lon_second)
            if curr_distance < shortest_dist:
                shortest_dist = curr_distance
                shortest_loc = loc2
        closest_locs.append((loc1, shortest_loc,shortest_dist))
    return closest_locs


def main():
    print("Enter the first array of geolocations:")
    locations1 = input("Format should be like 'lat1,lon1 lat2,lon2 ...' (e.g., '10.72,-15.07 20.23,-28.43'): ")
    locs1 = [(float(latitude), float(longitude)) for latitude, longitude in (loc.split(",") for loc in locations1.split())]

    print("\nEnter the second array of geolocations:")
    locations2 = input("Format should be like 'lat1,lon1 lat2,lon2 ...' (e.g., '10.17,-43.03 35.20,-10.13'): ")
    locs2 = [(float(latitude), float(longitude)) for latitude, longitude in (loc.split(",") for loc in locations2.split())]

    # Find shortest distances
    distances = find_shortest_distances(locs1, locs2)

    # Display results
    for point1, closest_point, distance in distances:
        print(f"Point 1: {point1} Closest Point: {closest_point} Distance: {distance:.2f} km")


if __name__ == "__main__":
    main()