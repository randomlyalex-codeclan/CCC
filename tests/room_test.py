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
    def test_room_has_unique_ID(self):
        pass

    
    #check room starts with no occupants
    def test_room_starts_with_no_occupants(self):
        self.assertEqual(0, len(self.room001.occupants))
        self.assertEqual(0, len(self.room002.occupants))
        self.assertEqual(0, len(self.room003.occupants))
        self.assertEqual(0, len(self.room004.occupants))
        self.assertEqual(False ,self.room004.occupied)

    #check occupancy
    def test_room_returns_true_occupancy(self):
        test_room = Room("Test Room", 10)
        test_room.occupants = list(range(2))
        self.assertEqual(len(test_room.occupants) > 0 ,test_room.check_occupancy())

    #test can empty
    def test_room_can_empty_occupants(self):
        test_room = Room("Test Room to empty", 15)
        test_room.occupants = [1,2,3,4]
        test_room.empty()
        self.assertEqual(False, test_room.check_occupancy())
        

    #test room starts with zero tab
    def test_room_starts_with_zero_tab(self):
        self.assertEqual(0.00, self.room002.tab)

    #test adding to room tab
    def test_room_tab_increases(self):
        test_room = Room("Test room tab", 10)
        test_room.add_to_tab(50.50)
        self.assertEqual(50.50, test_room.tab)