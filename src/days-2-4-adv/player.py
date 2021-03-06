# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, curRoom):
        self.name = name
        self.curRoom = curRoom
        self.inventory = []
    def __repr__(self):
        return f'Player {self.name}, {self.curRoom}, {self.inventory}'
    def __str__(self):
        return f'Player {self.name}, {self.curRoom}, {self.inventory}'
    def change_location(self, newRoom):
        self.curRoom = newRoom
    def add_item(self, item):
        self.inventory.append(item)
    def remove_item(self, item):
        self.inventory.remove(item)