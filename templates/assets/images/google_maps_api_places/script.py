from asyncore import write
import googlemaps
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

cordinates = [
(-27.5022, 153.044),
(-16.9414, 145.757),
(-27.4652, 153.027),
(-16.9461, 145.764),
(-27.065, 153.023),
(-24.2285, 151.919),
(-26.6847, 153.127),
(-23.3722, 150.504),
(-26.8356, 152.962),
(-16.8198, 145.633),
(-27.9548, 153.427)
]


#for export_names in export_names:
for export_names in export_names:
        img_link = str(export_names)
API_KEY = 'AIzaSyCJ4tabEYRktjzA9MRHM9EP-ZtNLh8GUpM'
gmaps = googlemaps.Client(key = API_KEY)
Cordinates = '-26.684744, 153.127442'
place_result = gmaps.places_nearby(location = Cordinates, radius = 40000, open_now = False)
my_place_id = place_result['results'][0]['place_id']
my_fields = ['photo']
place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
photo_id = place_details['result']['photos'][0]['photo_reference']
photo_width = 400
photo_height = 400
raw_image_data = gmaps.places_photo(photo_reference = photo_id, max_height = photo_height, max_width = photo_width)

def generate_location():
    f = open(img_link, 'wb')

    for chunk in raw_image_data:
        if chunk:
            f.write(chunk)  

    f.close()

generate_location()
