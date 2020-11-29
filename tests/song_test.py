import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song001 = Song("Shake It Off", "Taylor Swift","2000", "Pop", 150)
        self.song002 = Song("Stronger", "Kelly Clarkson","2000", "Pop", 145)
        self.song003 = Song("I Will Survive", "Gloria Gaynor","1970", "Disco", 140)
        self.song004 = Song("It’s Raining Men", "The Weather Girls", "1980", "Disco", 150)
        self.song005 = Song( "Single Ladies", "Beyoncé","2000", "R&B", 157)
        self.song006 = Song("Like a Virgin", "Madonna","1980", "Pop", 150)
        self.song007 = Song("Wrecking Ball", "Miley Cyrus","2010", "Pop", 150)
        self.song008 = Song("Emotions", "Mariah Carey","1990", "Pop", 150)
        self.song009 = Song("Rehab", "Amy Winehouse","2000", "Indie", 167)
        self.song010 = Song("Black Velvet", "Alannah Myles","1980", "Country", 150)
        self.song011 = Song("Son of a Preacher Man", "Dusty Springfield,", "1990", "Pop", 134)

        self.song012 = Song("Sweet Caroline", "Neil Diamond", "1990", "Rock", 150)
        self.song013 = Song("Don’t Stop Believin’", "Journey", "1980", "Rock", 150)
        self.song014 = Song("Bohemian Rhapsody", "Queen", "1970", "Rock", 152)
        self.song015 = Song("Wonderwall", "Oasis", "1990", "Pop", 136)
        self.song016 = Song("My Way", "Frank Sinatra", "1960", "Pop", 150)
        self.song017 = Song("I Wanna Be Sedated", "the Ramones", "1970", "Rock", 194)
        self.song018 = Song("Losing My Religion", "R.E.M.", "1990", "Pop", 150)
        self.song019 = Song("Never Gonna Give You Up", "Rick Astley", "1980", "Pop", 150)
        self.song020 = Song("Mack the Knife", "Bobby Darin", "1955", "Pop", 150)
        self.song021 = Song("If I Was Your Girlfriend", "Prince", "1980", "Funk", 175)

        self.song022 = Song("500 Miles", "The Proclaimers", "1980", "Classic", 151)
        self.song023 = Song("These Boots Are Made for Walking", "Nancy Sinatra", "1960", "Classic", 150)
        self.song024 = Song("Crazy", "Patsy Cline", "1960", "Classic", 150)
        self.song025 = Song("Happy", "Pharrell Williams", "2010", "Classic", 150)
        self.song026 = Song("Copacabana", "Barry Manilow", "1970", "Classic", 150)
        self.song027 = Song("That’s the Way (I Like It)", "KC and the Sunshine Band", "1990", "Classic", 150)
        self.song028 = Song("Celebration", "Kool and the Gang", "1960", "Classic", 167)
        self.song029 = Song("Funkytown", "Lipps, Inc", "1970", "Classic", 123)
        self.song030 = Song("Don’t Worry, Be Happy", "Bobby McFerrin", "1960", "Classic", 143)
        self.song031 = Song("Eye of the Tiger", "Survivor", "1980", "Classic", 150)

        #Q: is there a way to add these setup objects to a list for testing further down?

    #Test a Song has a name
    def test_song_has_title(self):
        self.assertEqual("Single Ladies", self.song005.title)
        


    #test artist
    def test_song_has_artist(self):
        self.assertEqual("Oasis", self.song015.artist)


    #Test a Song has a Song ID
    def test_song_has_unique_ID(self):
        # how?
        #maybe a for loop to check a if an ID is present in a list of the remainder? (would that work?)
        pass


    #Test a song has a genre
    # test its from a list of expected genres
    def test_song_has_genre(self):
        expected_genres = [
        "EDM",
        "Hip-hop",
        "Indie rock",
        "Jazz",
        "Metal",
        "Classic",
        "Pop",
        "Rap",
        "R&B",
        "Rock",
        "Disco"
        ]
        genre_exist = self.song022.genre in expected_genres
        self.assertEqual(True, genre_exist)


    #Test a Song has a sensible runtime
    # test its between 100 and 300 seconds?
    def test_song_has_sensible_runtime(self):
        runtime_sensible = 300 > self.song004.runtime > 100
        self.assertEqual(True, runtime_sensible)


    #Test year
    # test it starts 19 or 20, and ends with an int between 0 - 99
    def test_song_has_an_accepted_year(self):
        first_19_or_20 = (self.song004.year[:2] == "19" or "20")
        second_0_99 = 100 > int(self.song004.year[2:5]) >= 0
        accepted_year = first_19_or_20 and second_0_99
        self.assertEqual(True, accepted_year)





