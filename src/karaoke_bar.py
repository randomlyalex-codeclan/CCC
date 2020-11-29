class KaraokeBar:
    def __init__(self, name, rooms_list):
        self.name = name
        self.rooms_list = rooms_list
        self.till = 0

    def add_remove_guest_to_room_by_guest(self, guest, req_room): # should check the room is empty or not later
        for room in self.rooms_list:
            if guest in room.occupants:
                room.occupants.remove(guest)
                if len(room.occupants) == 0:
                    room.occupied = False
                return f"Removed from {room.name}"
        if req_room != None:
            for room in self.rooms_list: # I feel this can be refactored but i need advice. 
                if room == req_room and len(room.occupants) < room.capacity:
                    room.occupants.append(guest)
                    room.occupied = True
                    return f"Added to {room.name}"

    def search_for_guest(self, guest_to_search):
        for room in self.rooms_list:
            for occupant in room.occupants:
                if occupant == guest_to_search:
                    return room

    def add_remove_song_to_room_by_song(self, song_to_add, room_to_add): #should check the room has people in
        for room in self.rooms_list:
            if room == room_to_add and song_to_add not in room.songs_list:
                room.songs_list.append(song_to_add)
                return f"Added {song_to_add.title}"
            elif room == room_to_add and song_to_add in room.songs_list:
                room.songs_list.remove(song_to_add)
                return f"Removed {song_to_add.title}"

    def roll_call(self):
        roll_call = []
        for room in self.rooms_list:
            roll_call.extend(room.occupants)
        return roll_call

    def empty_room(self, room_to_empty):
        for room in self.rooms_list:
            if room == room_to_empty:
                room.occupants.clear()
                room.occupied = False
                return f"{room_to_empty} emptied"

    def find_empty_rooms(self):
        free_rooms = []
        for room in self.rooms_list:
            if room.occupied == False or len(room.occupants) == 0:
                free_rooms.append(room)
        return free_rooms

    def move_guests_between_rooms(self, room_from, room_to):
        for room in self.rooms_list:
            if room == room_to and room.occupied == False and room.capacity > len(room_from.occupants):
                middle_swap = room_from
                room_from = room_to
                room_to = middle_swap
                return True
        return False






