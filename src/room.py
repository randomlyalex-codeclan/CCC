class Room:
    ID = 0
    
    def __init__(self, name, capacity):
        self.name = name
        self.capcity = capacity
        Room.ID += 1
        self.occupied = False
        self.occupants = []
        self.tab = 0.00

    def check_occupancy(self):
        if self.occupants != []: self.occupied = True
        return len(self.occupants) > 0

    def empty(self):
        self.occupied = False
        self.occupants.clear()
        