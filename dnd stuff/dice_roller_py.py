#dice roller

import random


#roll a d4

def roll_d4():
    return random.randint(1, 4)

#roll a d6
def roll_d6():
    return random.randint(1, 6)

#roll a d8

def roll_d8():
    return random.randint(1, 8)

#roll a d12
def roll_d12():
    return random.randint(1, 12)

#roll a d20
def roll_d20():
    return random.randint(1, 20)

def roll_d100():
    return random.randint(1, 100)

print(roll_d100())