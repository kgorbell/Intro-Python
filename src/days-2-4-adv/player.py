# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, curRoom):
        self.name = name
        self.curRoom = curRoom
    def change_location(self, newRoom):
        self.curRoom = newRoom