# Exercise 8-6

# Creates a function for city and country.
def city_country(city, country):
    """Displays a city/country combination."""
    place = city + ", " + country

    return place

# Assigns each called city and country to a variable.
combination1 = city_country('Dublin', 'Ireland')
combination2 = city_country('Madison', 'USA')
combination3 = city_country('Toronto', 'Canada')

# Crete each country into a list of each city/country pair.
cities_and_countries = [combination1, combination2, combination3]

# Iterates through the list cities_and_countries and prints out each combination once.
for combination in cities_and_countries:
    print(combination)

# Exercise 8-7

def make_album(artist, album_name, track_count=''):
    """Returns a dictionary of album information."""
    album = {'artist': artist, 'album': album_name}
    if track_count:
        album['tracks'] = track_count

    return album

album_dictionary_1 = make_album('True Pirate', 'Wolves of the Sea')
album_dictionary_2 = make_album('Adrian Von Ziegler', 'Celtic Forest', 12)
album_dictionary_3 = make_album('Casting Spells', 'Whimsical Eve', 8)
album_dictionary_4 = make_album('Casting Spells', 'Majestic Mountain', 12)

album_collection = [album_dictionary_1, album_dictionary_2, album_dictionary_3, album_dictionary_4]

for album in album_collection:
    print(album)

# Exercise 8-8

def make_album(artist, album_name, track_count=''):
    """Returns a dictionary of album information."""
    album = {'artist': artist, 'album': album_name}
    if track_count:
        album['tracks'] = track_count

    return album

while True:
    print("\nPlease enter an artist name and album.")
    print("Optionally, feel free to enter the track count.")
    print("Enter 'q' at anytime to quit.")
    artist_name = input("Artist name: ")
    album_title = input("Album title: ")

    if artist_name == 'q':
        break

    if album_title == 'q':
        break

    album1 = make_album(artist_name, album_title)
    print(album1)
