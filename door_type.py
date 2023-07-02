import random

def generate_room():
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

    roll = random.randint(1, 100)
    for key in door_types.keys():
        if roll in key:
            return door_types[key]

    # Default case if roll is outside the defined ranges
    return {'material': 'Unknown', 'locked': False, 'stuck': False, 'trapped': False}
room = generate_room()
print(room)

