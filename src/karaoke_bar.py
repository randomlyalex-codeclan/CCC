class KaraokeBar:
    def __init__(self, name, rooms_list):
        self.name = name
        self.rooms_list = rooms_list
        self.till = 0

    def add_remove_guest_to_room_by_guest(self, guest, req_room):
        for room in self.rooms_list:
            if guest in room.occupants:
                room.occupants.remove(guest)
                return f"Removed from {room.name}"
        else:
            for room in self.rooms_list: # I feel this can be refactored but i need advice. 
                if room == req_room:
                    room.occupants.append(guest)
                return f"Added to {room.name}"

    def search_for_guest(self, guest_to_search):
        for room in self.rooms_list:
            for occupant in room.occupants:
                if occupant == guest_to_search:
                    return room

