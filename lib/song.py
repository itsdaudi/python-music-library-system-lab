class Song:
    # Class attributes - shared across ALL songs
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artists_count ={}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Call all class methods when a new song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

   