# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# Build the dictionary describing the album

def make_album(artist_name, album_title, number_of_tracks=''):
    """Build dictionary for album."""
    album = {'artist': artist_name, 'album': album_title}

    if number_of_tracks:
        album['n_tracks'] = number_of_tracks

    return album

album = make_album('2pac', 'the rose that grew from concrete')
print(album)

album = make_album('warren g', 'I want it all')
print(album)

album = make_album('50 cent', 'curtis')
print(album)

album = make_album('south central cartel', 'all day everyday', 17)
print(album)