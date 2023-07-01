import random

#first generate random rooms in a basic way
room_types = ['Cavern', 'Crypt', 'Library', 'Throne Room', 'Cell', 'Dock Area', 'Portcullis', 'DonJon']
monster_types = ['Orc', 'Skeleton', 'Manticore', 'Black Wyvern', 'Oni', 'Ghost', 'Vampire']
treasure_types = ['Sword of Execution', 'Javelin of Lightning', 'Wish Scroll', 'Grease']
trap_types = ['Pressure plate', 'Spike Trap', 'Oil Trap', 'Arrow Trap', 'Dud', 'Dud', 'dud', 'dud']

room_type = random.choice(room_types)
    has_monster = 