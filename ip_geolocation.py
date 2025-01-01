# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:39:25 2024

@author: IAN CARTER KULANI


"""


import os
import requests
import folium

print("======================================IP GEOLOCATION======================================\n")
def ping_server(ip):
    # Ping the server to check connectivity
    response = os.system(f"ping -c 1 {ip}")  # "-c 1" sends a single packet (Linux/Mac). Use "-n 1" on Windows.
    return response == 0

def get_location(ip):
    # Fetch geolocation info from a free API (e.g., IP-API)
    response = requests.get(f"http://ip-api.com/json/{ip}")
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return {
                "city": data["city"],
                "latitude": data["lat"],
                "longitude": data["lon"]
            }
    return None

def create_map(location):
    # Create a map centered on the server location
    map_obj = folium.Map(location=[location["latitude"], location["longitude"]], zoom_start=10)
    folium.Marker(
        [location["latitude"], location["longitude"]],
        popup=f"City: {location['city']}",
    ).add_to(map_obj)
    return map_obj

def main():
    ip = input("Enter the IP address of the server: ")
   
    # Ping the server
    if ping_server(ip):
        print(f"Successfully pinged {ip}")
       
        # Get the location of the server
        location = get_location(ip)
        if location:
            print(f"Server is located in {location['city']}, Lat: {location['latitude']}, Lon: {location['longitude']}")
           
            # Create and display map
            map_obj = create_map(location)
            map_obj.save("server_location_map.html")
            print("Map saved as server_location_map.html")
        else:
            print("Could not retrieve location data.")
    else:
        print(f"Could not ping {ip}. Server may be down or unreachable.")

if __name__ == "__main__":
    main()
    
   
print("==========================================================================================")