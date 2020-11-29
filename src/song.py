class Song:

    songID = 0

    def __init__(self, title, artist, year, genre, runtime):
        self.title = title
        self.artist = artist
        self.year = year
        self.genre = genre
        self.runtime = runtime
        Song.songID += 1         # increments a class variable as a songID


        