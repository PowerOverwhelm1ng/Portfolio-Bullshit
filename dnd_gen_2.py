import random

CHARACTER_TILES = {'stone': ' ',
 'floor': ' ',
 'wall': '#'
 }

class Generator:
    def __init__(self, width=64, height=64, max_rooms=15, min_room_xy=5,
        max_room_xy=10, rooms_overlap=False, random_connections=1, random_spurs=3, tiles=CHARACTER_TILES):
        self.width = width
        self.height = height
        self.max_rooms = max_rooms
        self.min_roomxy = min_room_xy
        self.max_room_xy = max_room_xy
        self.rooms_overlap = rooms_overlap
        self.random_connections = random_connections
        self.random_spurs = random_spurs
        self.tiles = CHARACTER_TILES
        self.level = []
        self.room_list = []
        self.corridor_list = []
        self.tiles_level = []

    def gen_room(self):
        x, y, w, h = 0, 0, 0, 0
        w = random.randint(self.min_roomxy, self.max_room_xy)
        h = random.randint(self.min_roomxy, self.max_room_xy)
        x = random.randint(1,(self.width -w -1))
        y = random.randint(1,(self.height -h -1))

        return [x, y, w, h]
    
    def room_overlapping(self, room, room_list):
        x = room[0]
        y = room[1]
        w = room[2]
        h = room[3]
        for current_room in room_list:
            # The rectangles don't overlap if
            # one rectangle's minimum in some dimension
            # is greater than the other's maximum in
            # that dimension.

            if (x < (current_room[0] + current_room[2]) and
                current_room[0] < (x + w) and
                y < (current_room[1] + current_room[3]) and
                current_room[1] < (y + h)):

                return True

        return False
