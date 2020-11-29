class KaraokeBar:
    def __init__(self, name, rooms_list):
        self.name = name
        self.rooms_list = rooms_list
        self.till = 0

    def add_remove_guest_to_room_by_guest(self, guest, req_room): # should check the room is empty or not later
        for room in self.rooms_list:
            if guest in room.occupants:
                room.occupants.remove(guest)
                return f"Removed from {room.name}"
        else:
            if req_room != None:
                for room in self.rooms_list: # I feel this can be refactored but i need advice. 
                    if room == req_room:
                        room.occupants.append(guest)
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
                return f"Added {song_to_add}"
            elif room == room_to_add and song_to_add in room.songs_list:
                room.songs_list.remove(song_to_add)
                return f"Removed {song_to_add}"





