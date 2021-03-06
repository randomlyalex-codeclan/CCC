import unittest
from src.karaoke_bar import KaraokeBar
from src.song import Song
from src.room import Room
from src.guest import Guest


class TestKaraokeBar(unittest.TestCase):

    def setUp(self):  
# rooms setup
        self.room001 = Room("Room 1", 10)
        self.room002 = Room("Room 2", 5)
        self.room003 = Room("Room 3", 20)
        self.room004 = Room("Room 4", 4) # the self within the unittesting really throws me, i think i need further talk over this.
        self.room005 = Room("Room 5", 7)
        self.room006 = Room("Room 6", 15)
        self.front_desk = Room("Front Desk", 30)

# setup a main test bar with rooms
        self.tone_deaf = KaraokeBar("Tone Deaf", [
            self.front_desk,
            self.room001,
            self.room002,
            self.room003,
            self.room004,
            self.room005,
            self.room006     
        ]
        )

# guests setup
        self.mark = Guest("Mark")
        self.ben = Guest("Ben", 1)
        self.jane = Guest("Jane", 2, "Wonderwall", 100.00)
        self.peter = Guest("Peter")
        self.john = Guest("John", 3)
        self.sally = Guest("Sally")
        self.dan = Guest("Dan")

# songs setup

        self.song001 = Song("Shake It Off", "Taylor Swift", "2000", "Pop", 150)
        self.song002 = Song("Stronger", "Kelly Clarkson", "2000", "Pop", 145)
        self.song003 = Song("I Will Survive", "Gloria Gaynor", "1970", "Disco", 140)
        self.song004 = Song("It’s Raining Men", "The Weather Girls", "1980", "Disco", 150)
        self.song005 = Song("Single Ladies", "Beyoncé", "2000", "R&B", 157)
        self.song006 = Song("Like a Virgin", "Madonna", "1980", "Pop", 150)
        self.song007 = Song("Wrecking Ball", "Miley Cyrus", "2010", "Pop", 150)
        self.song008 = Song("Emotions", "Mariah Carey", "1990", "Pop", 150)
        self.song009 = Song("Rehab", "Amy Winehouse", "2000", "Indie", 167)
        self.song010 = Song("Black Velvet", "Alannah Myles", "1980", "Country", 150)
        self.song011 = Song("Son of a Preacher Man","Dusty Springfield,", "1990", "Pop", 134)

        self.song012 = Song("Sweet Caroline", "Neil Diamond", "1990", "Rock", 150)
        self.song013 = Song("Don’t Stop Believin’","Journey", "1980", "Rock", 150)
        self.song014 = Song("Bohemian Rhapsody", "Queen", "1970", "Rock", 152)
        self.song015 = Song("Wonderwall", "Oasis", "1990", "Pop", 136)
        self.song016 = Song("My Way", "Frank Sinatra", "1960", "Pop", 150)
        self.song017 = Song("I Wanna Be Sedated","the Ramones", "1970", "Rock", 194)
        self.song018 = Song("Losing My Religion", "R.E.M.", "1990", "Pop", 150)
        self.song019 = Song("Never Gonna Give You Up","Rick Astley", "1980", "Pop", 150)
        self.song020 = Song("Mack the Knife", "Bobby Darin", "1955", "Pop", 150)
        self.song021 = Song("If I Was Your Girlfriend","Prince", "1980", "Funk", 175)

        self.song022 = Song("500 Miles", "The Proclaimers","1980", "Classic", 151)
        self.song023 = Song("These Boots Are Made for Walking","Nancy Sinatra", "1960", "Classic", 150)
        self.song024 = Song("Crazy", "Patsy Cline", "1960", "Classic", 150)
        self.song025 = Song("Happy", "Pharrell Williams","2010", "Classic", 150)
        self.song026 = Song("Copacabana", "Barry Manilow","1970", "Classic", 150)
        self.song027 = Song("That’s the Way (I Like It)","KC and the Sunshine Band", "1990", "Classic", 150)
        self.song028 = Song("Celebration", "Kool and the Gang", "1960", "Classic", 167)
        self.song029 = Song("Funkytown", "Lipps, Inc", "1970", "Classic", 123)
        self.song030 = Song("Don’t Worry, Be Happy","Bobby McFerrin", "1960", "Classic", 143)
        self.song031 = Song("Eye of the Tiger", "Survivor","1980", "Classic", 150)

# Test room name exists

    def test_room_name_exists(self):
        self.assertEqual("Front Desk", self.tone_deaf.rooms_list[0].name)

# Test room creation
    def test_room_creation(self):
        test_room_1 = Room("Test Name 1", 100)
        test_room_2 = Room("Galaxy far far away", 1000)
        test_karaoke_bar = KaraokeBar("All ears", [test_room_1, test_room_2])
        self.assertEqual("Galaxy far far away",
            test_karaoke_bar.rooms_list[1].name)

# Test search for guest 
    def test_search_guest_return_room(self):
        self.tone_deaf.rooms_list[0] = self.room001
        self.tone_deaf.rooms_list[1] = self.room002
        self.tone_deaf.rooms_list[2] = self.room003
        self.tone_deaf.rooms_list[1].occupants.append(self.mark)
        self.assertEqual(self.room002, self.tone_deaf.search_for_guest(self.mark))

# Test add a guest to a room they aren't in
    def test_add_remove_guest__to_empty_room(self):
        self.assertEqual("Added to Room 2", self.tone_deaf.add_remove_guest_to_room_by_guest(self.peter, self.room002))
        self.assertEqual(self.room002, self.tone_deaf.search_for_guest(self.peter))

#test add 1 people to a room
    def test_add_7_people_to_a_room(self):        
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.mark, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.ben, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.peter, self.room003)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.john, self.room004)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.jane, self.room005)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.sally, self.room006)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.dan, self.room002)
        self.assertEqual(self.room002, self.tone_deaf.search_for_guest(self.mark))

# Test add the same guest twice, which should remove them. 
    def test_add_remove_guest__to_room_with_them_in(self):
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.mark, self.room001)
        self.assertEqual("Removed from Room 1", self.tone_deaf.add_remove_guest_to_room_by_guest(self.mark, None))

#def test_add_guest_to_full_room(self): - ext

    def test_add_guest_to_full_room(self):
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.mark, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.ben, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.peter, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.john, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.jane, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.sally, self.room002)  #both of these shouldnt add
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.dan, self.room002)  #both of these should add
        self.assertEqual(5,len(self.tone_deaf.roll_call()))

# move guests between rooms test
    def test_move_guests_between_rooms(self):
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.mark, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.ben, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.peter, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.john, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.jane, self.room002)
        self.assertEqual(False, self.tone_deaf.move_guests_between_rooms(self.room002, self.room004)) # this should be rejected
        self.assertEqual(True, self.tone_deaf.move_guests_between_rooms(self.room002, self.front_desk)) # but then this should be allowed
        self.assertEqual(True, self.tone_deaf.move_guests_between_rooms(self.front_desk, self.room005)) # but then this should be allowed


# Test Add a song to a room it isn't in
    def test_add_song__to_room_by_song(self):
        self.tone_deaf.add_remove_song_to_room_by_song(self.song016, self.room002)
        self.assertEqual(True, self.song016 in self.tone_deaf.rooms_list[2].songs_list)

# Test the same with a few songs
    def test_add_a_few_songs__to_room_by_song(self):
        self.tone_deaf.add_remove_song_to_room_by_song(self.song010, self.room003)
        self.assertEqual("Added Shake It Off",self.tone_deaf.add_remove_song_to_room_by_song(self.song001, self.room003))
        self.tone_deaf.add_remove_song_to_room_by_song(self.song016, self.room002)
        self.assertEqual(True, self.song016 in self.tone_deaf.rooms_list[2].songs_list)

# Test Remove a song from a room it is already in
    def test_remove_song__to_room_by_song(self):
        self.tone_deaf.add_remove_song_to_room_by_song(self.song010, self.room003)
        self.tone_deaf.add_remove_song_to_room_by_song(self.song001, self.room003)
        self.tone_deaf.add_remove_song_to_room_by_song(self.song016, self.room002)
        self.assertEqual("Removed My Way", self.tone_deaf.add_remove_song_to_room_by_song(self.song016, self.room002))
        self.assertEqual(False, self.song016 in self.tone_deaf.rooms_list[2].songs_list)
    

# Test a roll call of guests
    def test_roll_call_of_guests(self):
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.mark, self.room001)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.ben, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.peter, self.room003)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.john, self.room004)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.jane, self.room005)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.sally, self.room006)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.dan, self.room002)
        self.assertEqual(7,len(self.tone_deaf.roll_call()))

# Test add a guest with friends to a room

# Test room empty

    def test_empty_room(self):
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.mark, self.room001)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.ben, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.peter, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.john, self.room004)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.jane, self.room005)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.sally, self.room006)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.dan, self.room002)
        self.assertEqual(7,len(self.tone_deaf.roll_call()))
        self.tone_deaf.empty_room(self.room002)
        self.assertEqual(4,len(self.tone_deaf.roll_call()))

# Test list of Empty rooms
    def test_return_empty_rooms(self):
        self.assertEqual(6,len(self.tone_deaf.find_empty_rooms()))

# test empty rooms after adding and removing and then emptying a room
    def test_return_empty_rooms_better(self):
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.mark, self.room001)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.ben, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.peter, self.room002)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.john, self.room004)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.jane, self.room005)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.sally, self.room006)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.dan, self.room002)
        self.tone_deaf.empty_room(self.room002)
        self.assertEqual([self.room002,self.room003],self.tone_deaf.find_empty_rooms())
        
#favourite song test
    def test_guests_fav_song_is_in_the_room(self):
        self.tone_deaf.add_remove_song_to_room_by_song(self.song010, self.room005)
        self.tone_deaf.add_remove_song_to_room_by_song(self.song001, self.room005)
        self.tone_deaf.add_remove_song_to_room_by_song(self.song016, self.room005)
        self.tone_deaf.add_remove_song_to_room_by_song(self.song015, self.room005)
        self.assertEqual("Whoo! Fav Track!",self.tone_deaf.add_remove_guest_to_room_by_guest(self.jane, self.room005))

# test main guest paying for 1 hour
    def test_guest_paying_for_1_hour(self):
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.peter, self.front_desk)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.john, self.front_desk)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.jane, self.front_desk)
        self.tone_deaf.add_remove_guest_to_room_by_guest(self.sally, self.front_desk)
        self.tone_deaf.pay_for_time_and_room(self.jane, 1, self.room005, self.front_desk)
        self.assertEqual(60.00, self.jane.wallet)
        self.assertEqual(40.00, self.tone_deaf.till)
        self.assertEqual(4, len(self.room005.occupants))

# Test add a list of song id's to a room
# Test check list of songs time, and dont allow more songs than time on the room
# Test Add a genre to a room
# Test Add an artist to a room
# Test add a decade to a room
# Test add a year group that doesnt exist
# test itemised_tab as dictionary of key: guest / value: money owed. total of this passes to current tab attribute.
# test buying food/drink

