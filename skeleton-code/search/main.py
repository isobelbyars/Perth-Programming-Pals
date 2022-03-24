"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import sys
import json

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from search.util import create_board_dict, print_board, print_coordinate


def a_star_search(data):
    #TODO
    # function needs to return the path cost
    # function needs to retunr the grid sequence [for-looped print statement]
    # 0 if no solution exists

    # Board Parameters
    n = data.get('n')
    board_dict = create_board_dict(data)
    start = data.get('start')
    goal = data.get('goal')

    print('n',n, '\nbd ', board_dict, '\ns', start, '\ng', goal)




def heuristic(y_coord, x_coord):
    #TODO
    # This function returns the direct distance from a particular cell to the goal cell
    # y_coord: represents the vertical coordinate 
    # x_coord: " " horizontal coordinate





def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)
   
    #board_dict=create_board_dict(data)
    #a_star_search(data)

    print (data)

    """bd = {
        (0, 4): "hello",
        (1, 1): "r",
        (1, 2): "b",
        (3, 2): "$",
        (2, 3): "***"}"""

    print_board(data['n'],board_dict)
    # TODO: DONE
    # Find and print a solution to the board configuration described
    # by `data`. 
    # Why not start by trying to print this configuration out using the
    # `print_board` helper function? (See the `util.py` source code for
    # usage information).
