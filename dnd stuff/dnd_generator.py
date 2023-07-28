import random
import cairo
#first generate random rooms in a basic way
def main():

    def generate_room():

        room_types = ['Cavern', 'Crypt', 'Library', 'Throne Room', 'Cell', 'Dock Area', 'Portcullis', 'DonJon']
        monster_types = ['Orc', 'Skeleton', 'Manticore', 'Black Wyvern', 'Oni', 'Ghost', 'Vampire']
        treasure_types = ['Sword of Execution', 'Javelin of Lightning', 'Wish Scroll', 'Grease']
        trap_types = ['Pressure plate', 'Spike Trap', 'Oil Trap', 'Arrow Trap', 'Dud', 'Dud', 'dud', 'dud']

        room_type = random.choice(room_types)
        has_monster =  random.choice(True, False)
        monster = random.choice(monster_types) if has_monster else None
        has_treasure = random.choice([True, False])
        treasure = (treasure_types) if has_treasure else None
        has_trap = random.choice([True, False])
        trap = random.choice(trap_types) if has_trap else None

        room = {
            "room_type": room_type,
            "has_monster": has_monster,
            "monster": monster,
            "has_treasure": has_treasure,
            "treasure": treasure,
            "has_trap": has_trap,
            "trap": trap
        }
        return room
    def display_room(room):
        print("Room Type: ", room["room_type"])
