from room import Room
from player import Player
from item import Item
# Declare all the rooms


class bcolors:
    HEADER = '\033[95m'
    OKRED = '\033[91m'
    OKGREY = '\033[90m'
    OKBLUE = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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


shovel = Item("shovel", "It digs señor!")
axe = Item("axe", "Try not to throw it!")
knife = Item("knife", "Stabs things.")
gun = Item("gun", "It shoots bullets!")
bottle = Item("bottle", "You can drink liquid out of it.")
hat = Item("hat", "The coolest thing to wear these days!")
pen = Item("pen", "It shoots out ink!")
chest = Item("chest", "You will never know whats inside!")


room['outside'].add_item(shovel)
# room['outside'].add_item(axe)
# room['foyer'].add_item(shovel)
room['foyer'].add_item(gun)
room['overlook'].add_item(bottle)
# room['overlook'].add_item(hat)
# room['narrow'].add_item(hat)
room['narrow'].add_item(pen)
room['treasure'].add_item(chest)

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
def found_item():
    for item in andrew.current_room.items:
        print(bcolors.OKGREEN + "\nYou found a {}!\n".format(item.name) + bcolors.ENDC)
        pick_up = input(bcolors.OKBLUE +
                        "Please type the item you would like to pick up. \nInsert [take] [name of item] or type no.\n\nEnter here:" + bcolors.ENDC)
        if pick_up == "take {}".format(item.name):
            andrew.current_room.remove_item(item)
            andrew.pickup_item(item)
            print(bcolors.OKGREEN +
                  "\nYou have picked up a {}\n".format(item.name) + bcolors.ENDC)


def dropped_item():

    for item in andrew.inventory:
        drop = input(bcolors.OKBLUE +
                     "Would you like to drop an item? \nInsert [drop] [name of item] or type no.\n\nEnter here:" + bcolors.ENDC)
        if drop == "drop {}".format(item.name):
            andrew.drop_item(item)
            andrew.current_room.add_item(item)


def warning_message():
    print(bcolors.WARNING +
          "\nWARNING there seems to be no room in that path!\n")


def welcome_message():
    welcome_message = f'\n{bcolors.HEADER}{bcolors.BOLD}Welcome to andrews lost treasure! \nIt is up to you to find the lost treasure!{bcolors.ENDC}{bcolors.ENDC}\n'
    print(welcome_message)


def location():
    print(
        f"\n{bcolors.OKGREEN }You are now in {andrew.current_room.name} {bcolors.ENDC}\n")
    print(bcolors.HEADER + andrew.current_room.description + bcolors.ENDC)


welcome_message()

andrew = Player("Andrew", room['outside'])
print(f"{bcolors.OKGREEN}{andrew.name}, You are at the,{andrew.current_room.name} \nwhere to now?{bcolors.ENDC}\n")
# found_item()
while True:
    move = input(
        f"{bcolors.OKBLUE}\n[i] Check Inventory \n[n] North \n[e] East \n[s] South \n[w] West \n[q] Quit\n\nEnter here:{bcolors.ENDC}")
    # player moves to foyer by clicking "n"
    if move == "q":
        print("\nFarewell Good Sir\n")
        quit()

    if move == "i":
        if len(andrew.inventory) > 0:
            print(bcolors.OKGREEN +
                  "\nHere is a inventory of your items:" + bcolors.ENDC)
            for item in andrew.inventory:
                print(bcolors.UNDERLINE + bcolors.BOLD +
                      "a {}".format(item.name) + bcolors.ENDC)
                drop = input(bcolors.OKBLUE +
                             "\nWould you like to drop an item? \nInsert [drop] [name of item] or type no.\n\nEnter here:" + bcolors.ENDC)
            if drop == "drop {}".format(item.name):
                andrew.drop_item(item)
                andrew.current_room.add_item(item)
                print(
                    bcolors.OKGREEN + "\nYou have dropped a {}\n".format(item.name) + bcolors.ENDC)
        else:
            print(bcolors.OKRED + "\nYou have no items yet!\n" + bcolors.ENDC)
    if move == "n":
        if andrew.current_room.n_to == None:
            warning_message()
        else:
            andrew.current_room = andrew.current_room.n_to
            location()
            found_item()
    elif move == "e":
        if andrew.current_room.e_to == None:
            warning_message()
        else:
            andrew.current_room = andrew.current_room.e_to
            location()
            found_item()
    elif move == "s":
        if andrew.current_room.s_to == None:
            warning_message()
        else:
            andrew.current_room = andrew.current_room.s_to
            location()
            found_item()
    elif move == "w":
        if andrew.current_room.w_to == None:
            warning_message()
        else:
            andrew.current_room = andrew.current_room.w_to
            location()
            found_item()

print("please continue")
