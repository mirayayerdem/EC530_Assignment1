# EC530_Assignment1
# Author: Miray Ayerdem
This function takes two arrays of geolocations and matches each point in the first array to the closest point in the second array using the Haversine formula to calculate distances.

# **Requirements**
Python 3.6 or higher

# **How to Use**

1. Clone the repository => git clone https://github.com/mirayayerdem/EC530_Assignment1.git  
2. Go to this folder => cd EC530_Assignment1  
3. Run your script in this format:  
4. Enter <lat,lon> for each location and add a space for additional locations: python find_distance.py --locations1 "lat1,lon1 lat2,lon2 ..." --locations2 "lat3,lon3 lat4,lon4 ..."  
Example Script: python find_distance.py --locations1 "20.4176,-14.0074 17.0525,-8.7434" --locations2 "17.7729,-122.4118 65.1681,-80.2988"  



