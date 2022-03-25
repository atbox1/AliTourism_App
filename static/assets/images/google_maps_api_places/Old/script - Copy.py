from asyncore import write
from io import BytesIO
from urllib import response
from PIL import Image
import chunk
import googlemaps
import shutil
import requests
import itertools

export_names = [
'BlackCard Cultural Tours.jpg',
'Coral Expeditions - Cape York and Arnhem Land.jpg',
'Birrunga Gallery and Dining.jpg',
'Bama Way Aboriginal Journeys (Adventure North).jpg ',
'Abbey Museum of Art & Archaeology.jpg',
'Agnes Water Museum.jpg',
'Aquaduck Sunshine Coast.jpg',
'Archer Park Rail Museum.jpg',
'Australia Zoo.jpg',
'Australian Butterfly Sanctuary.jpg',
'Australian Whale Watching.jpg']

cordinates_lists = [
'-27.5022, 153.044',
'-16.9414, 145.757',
'-27.4652, 153.027',
'-16.9461, 145.764',
'-27.065, 153.023',
'-24.2285, 151.919',
'-26.6847, 153.127',
'-23.3722, 150.504',
'-26.8356, 152.962',
'-16.8198, 145.633',
'-27.9548, 153.427'
]

i = 0
while i<11:
    for cordinate_list in cordinates_lists:
        cordinates = str(cordinate_list)
    for export_name in export_names:
        img_link = str(export_name)
    API_KEY = 'APIKEY'
    gmaps = googlemaps.Client(key = API_KEY)
    place_result = gmaps.places_nearby(location = str(cordinates), radius = 40000, open_now = False)
    my_place_id = place_result['results'][0]['place_id']
    my_fields = ['photo']
    place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
    photo_id = place_details['result']['photos'][0]['photo_reference']
    photo_width = 400
    photo_height = 400
    raw_image_data = gmaps.places_photo(photo_reference = photo_id, max_height = photo_height, max_width = photo_width)
    
    def download_image(photo_id):
        response = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={photo_id}APIKEY".format(photo_id=photo_id)
        picture_name = open(img_link, "wb")
        picture_name.write(response.content)
        picture_name.close()
    
    i += 1

    #def generate_location(img_link, raw_image_data):
        #someString = raw_image_data
        #f = open(img_link, 'wb')
        #f.write(someString + r'\r\n\\')
        #f.close()

    #def generate_location():
        #f = open(img_link, 'wb')

        #for chunk in raw_image_data:
            #if chunk:
                #f.write(chunk)  

        #f.close()
    
    #generate_location()
    #download_image(photo_id)
   
    

