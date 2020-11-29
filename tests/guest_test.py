import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.mark = Guest("Mark")
        self.ben = Guest("Ben",1)
        self.jane = Guest("Jane",2, "Wonderwall", 100.00)
        self.peter = Guest("Peter")
        self.john = Guest("John", 3)
        self.sally = Guest("Sally")
        self.dan = Guest("Dan")

    #Test a Guest has a name
    def test_guest_has_a_name(self):
        self.assertEqual("Mark", self.mark.name)

    #Test a Guest has a member ID or is in a Guest friends list
    def test_guest_has_an_negative_ID(self):
        self.assertEqual(0, self.mark.member_id)
    
    def test_member_has_an_ID(self):
        self.assertEqual(1, self.ben.member_id)

    def test_member_has_an_ID__2(self):
        self.assertEqual(2, self.jane.member_id)

    #Test a Guest hasd a wallet - ext
    #Test add and remove money from wallet  -ext
    #Test a favourite song - ext