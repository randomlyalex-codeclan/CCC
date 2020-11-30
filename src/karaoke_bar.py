class KaraokeBar:
    def __init__(self, name, rooms_list):
        self.name = name
        self.rooms_list = rooms_list
        self.till = 0
        self.rate = 40.00

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
                    for song in room.songs_list:
                        if guest.fav_song == (song.title or song.artist):
                            return "Whoo! Fav Track!"
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
        # self.rooms_list[0].occupied = True
        # self.rooms_list[0].occupants = [1]
        for room in self.rooms_list:
            if (room.occupied == False or len(room.occupants) == 0) and room != self.rooms_list[0]: # this is super hacky, help. :)
                free_rooms.append(room)
        return free_rooms

    def move_guests_between_rooms(self, room_from, room_to):
        for room in self.rooms_list:
            if room == room_to and room.occupied == False and room.capacity > len(room_from.occupants):
                room_to.occupants = room_from.occupants
                room.occupied = True
                self.empty_room(room_from)              
                return True
        return False

    def pay_for_time_and_room(self, paying_guest, time_in_h, room_to_book, front_desk):
        #check room to book is empty
        cost = time_in_h * self.rate
        if room_to_book.occupied == False:
            if paying_guest.wallet > cost:  #check the guest has enough money for the time
                if self.move_guests_between_rooms(front_desk, room_to_book) != False: #check the frontdesk  will fit in room to book and move to room to book
                    self.move_guests_between_rooms(front_desk, room_to_book)
                    paying_guest.wallet -= cost
                    self.till += cost
#                    self.timer += time_in_h
                    return "Enjoy your night!"

        # ≈ add their songs (figure this out later)







