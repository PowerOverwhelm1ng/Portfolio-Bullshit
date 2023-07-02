def generate_room():
    room_types = {
            (1, 8): {'material': 'Wooden', 'quality': 'Simple', 'locked': False, 'stuck': False, 'trapped': False},
            (9, 9): {'material': 'Wooden', 'quality': 'Simple', 'locked': False, 'stuck': False, 'trapped': True},
            (10, 23): {'material': 'Wooden', 'quality': 'Simple', 'locked': False, 'stuck': True, 'trapped': False},
            (24, 24): {'material': 'Wooden', 'quality': 'Simple', 'locked': False, 'stuck': True, 'trapped': True},
            (25, 29): {'material': 'Wooden', 'quality': 'Simple', 'locked': True, 'stuck': False, 'trapped': False},
            (30, 30): {'material': 'Wooden', 'quality': 'Simple', 'locked': True, 'stuck': False, 'trapped': True},
            (31, 35): {'material': 'Wooden', 'quality': 'Good', 'locked': False, 'stuck': False, 'trapped': False},
            (36, 36): {'material': 'Wooden', 'quality': 'Good', 'locked': False, 'stuck': False, 'trapped': True},
            (37, 44): {'material': 'Wooden', 'quality': 'Good', 'locked': False, 'stuck': True, 'trapped': False},
            (45, 45): {'material': 'Wooden', 'quality': 'Good', 'locked': False, 'stuck': True, 'trapped': True},
            (46, 49): {'material': 'Wooden', 'quality': 'Good', 'locked': True, 'stuck': False, 'trapped': False},
            (50, 50): {'material': 'Wooden', 'quality': 'Good', 'locked': True, 'stuck': False, 'trapped': True},
            (51, 55): {'material': 'Wooden', 'quality': 'Strong', 'locked': False, 'stuck': False, 'trapped': False},
            (56, 56): {'material': 'Wooden', 'quality': 'Strong', 'locked': False, 'stuck': False, 'trapped': True},
            (57, 64): {'material': 'Wooden', 'quality': 'Strong', 'locked': False, 'stuck': True, 'trapped': False},
            (65, 65): {'material': 'Wooden', 'quality': 'Strong', 'locked': False, 'stuck': True, 'trapped': True},
            (66, 69): {'material': 'Wooden', 'quality': 'Strong', 'locked': True, 'stuck': False, 'trapped': False},
            (70, 70): {'material': 'Wooden', 'quality': 'Strong', 'locked': True, 'stuck': False, 'trapped': True},
            (71, 71): {'material': 'Stone', 'locked': False, 'stuck': False, 'trapped': False},
            (72, 72): {'material': 'Stone', 'locked': False
            }

roll = random.randint(1, 100)
    for key in door_types.keys():
        if roll in key:
            return door_types[key]

    # Default case if roll is outside the defined ranges
    return {'material': 'Unknown', 'locked': False, 'stuck': False, 'trapped': False}