import random
import numpy

# FUNC to define game, with 3 doors
def game(winningdoor, selected_door, change=False):
    assert winningdoor < 3
    assert winningdoor >= 0

    # presenter removes the first door that was NOT selected
    remove_door = next(i for i in range(3) if i != selected_door and i != winningdoor)

    # contestant decides to change their choice
    if change:
        selected_door = next(i for i in range(3) if i != selected_door and i != remove_door)

    # Check if the selected door matches the winning door
    return selected_door == winningdoor

if __name__ == '__main__':
    player_doors = numpy.random.randint(0, 2 * (1000 * 1000 * 1), size=1000000)

    winning_doors = [d for d in player_doors if game(1, d)]
    print("Winning percentage without changing choice: ", len(winning_doors) / len(player_doors))

    winning_doors = [d for d in player_doors if game(1, d, change=True)]
    print("Winning percentage while changing choice: ", len(winning_doors) / len(player_doors))
