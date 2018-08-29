from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player('Samwise', room['foyer'])
# print(player1.curRoom.name)
# player1.curRoom = player1.curRoom.n_to
# print(player1.curRoom.name)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print("""{} is currently in {}:
    {}
    Please input a new direction (n, e, s, or w) for {}, or enter \'quit\' to exit the game.""".format(player1.name, player1.curRoom.name, player1.curRoom.description, player1.name))
    userInput = input()

    if userInput == 'quit':
        print('Thanks for playing, have a nice day!')
        exit()
    elif userInput in ['n', 'e', 's', 'w']:
        newRoom = player1.curRoom.getRoomInDirection(userInput)
        if newRoom == None:
            print('You cannot move in this direction')
        else:
            player1.change_location(newRoom)
    else:
        print('INVALID INPUT: please input a proper command for {}'.format(player1.name))