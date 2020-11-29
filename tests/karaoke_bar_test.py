import unittest
from src.karaoke_bar import KaraokeBar
from src.song import Song
from src.room import Room
from src.guest import Guest

class TestKaraokeBar(unittest.TestCase):
    
    def setUp(self):
        room001 = Room("Room 1", 10) # remind me why these don't need self. the self instance throws me a fair bit in testing.
        room002 = Room("Room 2", 5)
        room003 = Room("Room 3", 20)
        room004 = Room("Room 4", 4)
        room005 = Room("Room 5", 7)
        room006 = Room("Room 6", 15)
        self.tone_deaf = KaraokeBar("Tone Deaf", [room001, room002, room003, room004, room005, room006] )

    #Test create a room
    #Test a roll call of guests
    #Test add a guest to a room
    #Test add a guest with friends to a room
    #Test room empty
    #Test list of Empty rooms
    #Test Add a song to a room
    #Test Add a genre to a room
    #Test Add an artist to a room
    #Test add a decade to a room
    #Test add a year group that doesnt exist
    #
