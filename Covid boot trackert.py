import folium
#Extraire les donnes
def scraper():
    print("Data Extration successful")
#afficher les infos sur map
def maper():
    latlng = [33.555555, -7.555555]
    map = folium.Map(location=latlng)
    folium.Marker(location=latlng, popup='casablnca: 123').add_to(map)
    folium.CircleMarker(location=latlng, radius=50, fill=True).add_to(map)
    map.save("index.html")

    print("Mapping successful")
#Appel des fonction
scraper()
maper()