import random
from random import seed, randint
import numpy
#FUNC to define game, with 3 doors
def game(winningdoor, selected_door, change=False):
    assert winningdoor < 3
    assert winningdoor >= 0

    #presenter removes first door that was NOT selected
    remove_door= next(i for i in range(3)if i != selected_door and i != winningdoor)

    #contestant decides to change their choice
    if change:
        selected_door = next(i for i in range(3)if i != selected_door and i != remove_door)


    # if the player never changes their choice
    return  selected_door

if __name__ == '__main__':
    player_doors = numpy.random.random_integers(0, 2 * (1000 * 1000 * 1))

    winning_doors = [d for d in player_doors if game(1, d)]
    print("Winning percentage without changing choice: ", len(winning_doors)/len(player_doors))    

    winning_doors = [d for d in player_doors if game(1,d,change=True)]
    print("Winning percentage whole changing choice: ", len(winning_doors)/ len(player_doors))         