import random


door_types = {
        range(1, 9): {'material': 'Wooden', 'quality': 'Simple', 'locked': False, 'stuck': False, 'trapped': False},
        range(9, 10): {'material': 'Wooden', 'quality': 'Simple', 'locked': False, 'stuck': False, 'trapped': True},
        range(10, 24): {'material': 'Wooden', 'quality': 'Simple', 'locked': False, 'stuck': True, 'trapped': False},
        range(24, 25): {'material': 'Wooden', 'quality': 'Simple', 'locked': False, 'stuck': True, 'trapped': True},
        range(25, 30): {'material': 'Wooden', 'quality': 'Simple', 'locked': True, 'stuck': False, 'trapped': False},
        range(30, 31): {'material': 'Wooden', 'quality': 'Simple', 'locked': True, 'stuck': False, 'trapped': True},
        range(31, 36): {'material': 'Wooden', 'quality': 'Good', 'locked': False, 'stuck': False, 'trapped': False},
        range(36, 37): {'material': 'Wooden', 'quality': 'Good', 'locked': False, 'stuck': False, 'trapped': True},
        range(37, 45): {'material': 'Wooden', 'quality': 'Good', 'locked': False, 'stuck': True, 'trapped': False},
        range(45, 46): {'material': 'Wooden', 'quality': 'Good', 'locked': False, 'stuck': True, 'trapped': True},
        range(46, 50): {'material': 'Wooden', 'quality': 'Good', 'locked': True, 'stuck': False, 'trapped': False},
        range(50, 51): {'material': 'Wooden', 'quality': 'Good', 'locked': True, 'stuck': False, 'trapped': True},
        range(51, 56): {'material': 'Wooden', 'quality': 'Strong', 'locked': False, 'stuck': False, 'trapped': False},
        range(56, 57): {'material': 'Wooden', 'quality': 'Strong', 'locked': False, 'stuck': False, 'trapped': True},
        range(57, 65): {'material': 'Wooden', 'quality': 'Strong', 'locked': False, 'stuck': True, 'trapped': False},
        range(65, 66): {'material': 'Wooden', 'quality': 'Strong', 'locked': False, 'stuck': True, 'trapped': True},
        range(66, 70): {'material': 'Wooden', 'quality': 'Strong', 'locked': True, 'stuck': False, 'trapped': False},
        range(70, 71): {'material': 'Wooden', 'quality': 'Strong', 'locked': True, 'stuck': False, 'trapped': True},
        range(71, 72): {'material': 'Stone', 'locked': False, 'stuck': False, 'trapped': False},
        range(72, 73): {'material': 'Stone', 'locked': False, 'stuck': False, 'trapped': False}
        }
room_chamber_size = {
        range(1, 3): 'Square, 8 x 8 squares',
        range(3, 5): 'Square, 10 x 10 squares',
        range(5, 7): 'Rectangle, 6 x 8 squares',
        range(7, 9): 'Rectangle, 8 x 10 squares',
        range(9, 11): 'Rectangle, 10 x 16 squares',
        range(11, 13): 'Octagon, 8 x 8 squares',
        range(13, 15): 'Octagon, 8 x 12 squares',
        range(15, 17): 'Octagon, 12 x 12 squares',
        range(17, 19): 'Irregular, roughly 8 x 10 squares',
        range(19, 21): 'Irregular, roughly 10 x 16 squares'
    }

def get_chamber_size():
    roll = random.randint(1, 20)
    for key in room_chamber_size.keys():
        if roll in key:
            return room_chamber_size[key]

        # Default case if roll is outside the defined ranges


def generate_room():
    roll = random.randint(1, 100)
    for key in door_types.keys():
        if roll in key:
            return door_types[key]


    
        # Default case if roll is outside the defined ranges
    default_door = {'material': 'Unknown', 'quality': 'Unknown', 'locked': False, 'stuck': False, 'trapped': False}
    room = {
            'door': 'Unknown',
            'chamber_size': get_chamber_size()
        }
    return room

def main():
    room = generate_room()
    print(room)

main()