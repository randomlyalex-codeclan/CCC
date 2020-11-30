class Guest:
    # member_id = 0
    def __init__(self, name, member_id = None, fav_song = None, wallet = None, friends_list = None):
        self.name = name
        if fav_song == None:
            fav_song = ''
        else: 
            self.fav_song = fav_song
        if member_id == None:
            self.member_id = 0
        else:
            self.member_id = member_id
        #    self.member_id = Guest.member_id # I wanted to add an incremental counter here that only incremented for members, i couldnt get it to work.
        #    Guest.member_id = self.member_id + 1
        if wallet == None: 
            self.wallet = 0
        else: 
            self.wallet = wallet
        if friends_list == None: 
            self.friends_list = []
        else:
            self.friends = friends_list
        #remember to to consider member ID relationship between members and guests etc... 
        
 