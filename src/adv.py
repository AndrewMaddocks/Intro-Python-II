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


# start of game
# welcome player find the treasure
# user choice of where to go [n][e][s][w][q]
def welcome_message():
    welcome_message = 'Welcome to andrews lost treasure! \nIt is up to you to find the lost treasure!'
    print(welcome_message)


welcome_message()

andrew = Player("Andrew", room['outside'])
print(andrew.name, "You are at", andrew.current_room.name, "where to now?")


while True:
    move = input("[n] North [e] East [s] South [w] West [q] Quit\n")
    # player moves to foyer by clicking "n"
    if move == "q":
        print("Farewell Good Sir")
        quit()
    if move == "n":
        if andrew.current_room.n_to == None:
            print("warning there seems to be no room in that path!")
        else:
            andrew.current_room = andrew.current_room.n_to
            print(andrew.current_room.name)
            print(andrew.current_room.description)
    elif move == "e":
        if andrew.current_room.e_to == None:
            print("warning there seems to be no room in that path!")
        else:
            andrew.current_room = andrew.current_room.e_to
            print(andrew.current_room.name)
            print(andrew.current_room.description)
    elif move == "s":
        if andrew.current_room.s_to == None:
            print("warning there seems to be no room in that path!")
        else:
            andrew.current_room = andrew.current_room.s_to
            print(andrew.current_room.name)
            print(andrew.current_room.description)
    elif move == "w":
        if andrew.current_room.w_to == None:
            print("warning there seems to be no room in that path!")
        else:
            andrew.current_room = andrew.current_room.w_to
            print(andrew.current_room.name)
            print(andrew.current_room.description)

print("please continue")
