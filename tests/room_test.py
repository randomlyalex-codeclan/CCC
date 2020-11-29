import unittest
from src.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room001 = Room("Room 1", 10)
        self.room002 = Room("Room 2", 5)
        self.room003 = Room("Room 3", 20)
        self.room004 = Room("Room 4", 4)
        self.room005 = Room("Room 5", 7)
        self.room006 = Room("Room 6", 15)

    #test a room has an ID
    #Test a room has a list of guests
    #Test guests can be add or removed
    #Test a room has a list of songs
    #Test songs can be add or removed
    #test room capacity full - ext
    #test adding to room tab