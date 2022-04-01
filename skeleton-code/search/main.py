"""
COMP30024 Artificial Intelligence, Semester 1, 2022
Project Part A: Searching

This script contains the entry point to the program (the code in
`__main__.py` calls `main()`). Your solution starts here!
"""

import sys
import json
from operator import itemgetter

# If you want to separate your code into separate files, put them
# inside the `search` directory (like this one and `util.py`) and
# then import from them like this:
from search.util import create_board_dict, print_board, print_coordinate


def a_star_search(data):
    # This is the primary a* search algorithm 
    # Upon identifying the goal state, it calls print_result(...) to print the results

    # Board Parameters
    n = data.get('n')
    board_dict = create_board_dict(data)
    start = data.get('start')
    goal = data.get('goal')

    g_cost = 0 # actual path cost to current tile
    h_cost = 0 # est. path cost to goal tile from current tile
    f_cost = 0 # g_cost + h_cost
    
    f_start = g_cost + heuristic(start,goal)
    start_node=[]
    start_node.append(start)
    start_node.append([-1,-1])
    start_node.append(g_cost) # Add the heuristic distance to the start tile
    start_node.append(f_start)

    unexplored = [start_node] # [ [[4, 2], [0, 0], 0, 6] ]
    explored = []
    current = start_node # current tile

    # Max coordinate values based on grid size
    x_max = n-1
    y_max = n-1

    # Boolean flag denoting if the goal state was found
    success = False 

    while unexplored: # while there are unexplored nodes
        unexplored = sorted(unexplored, key=itemgetter(3)) # sort by the f_value
        current = unexplored.pop(0) # [[4, 2], [0, 0], 0, 6] 

        #*if this is our destination node then return
        if current[0] == goal:
            success = True
            break

        # put the current tile in the exlplored list
        explored.append(current) # just add the grid coordinates 
        
        # look at all neighboring unexplored cells 
        y_delta=1
        x_delta=0
        for k in range(6): # at most 6 neighboring unexplored tiles
            # loops clockwise around the current coord. 
            # linear transformation to change coordinates to explore the next neighbour
            temp = y_delta + x_delta
            y_delta = -1*x_delta
            x_delta = temp

            neighbour_coord = [current[0][0]+y_delta, current[0][1]+x_delta] # neighboring tile
            exp_coord_list = [item[0] for item in explored] # a list of coords of tiles explored
            unexp_coord_list = [item[0] for item in unexplored]

            #Do stuff
            if neighbour_coord[0] > y_max or neighbour_coord[1] > x_max or neighbour_coord[0]<0 or neighbour_coord[1]<0:
                continue
                # out of bound of the grid space
            
            elif neighbour_coord in exp_coord_list or tuple(neighbour_coord) in list(board_dict.keys()):
                continue
                # tile has been explored OR tile is an obstacle
            
            
            # Consider alternative paths evaluating discovered path costs
            else: 
                # Explored List
                if neighbour_coord in exp_coord_list:
                    n_idx = exp_coord_list.index(neighbour_coord) # return the idx of the neighbour coord
                    if explored[n_idx][2]+1 < current[2]: # compare a explored neighbours g score +1  and current node g value to see if going through the explored neighbour is a shorter path
                        current[2] = explored[n_idx][2]+1 # shorter actual path
                        current[1] = neighbour_coord # change the parent 
                    
                    else:
                        # No need to re-explore - cost is the same or worse
                        continue
                # Unexplored List
                elif neighbour_coord in unexp_coord_list:
                    n_idx = unexp_coord_list.index(neighbour_coord) # return the idx of the neighbour coord
                    if unexplored[n_idx][2] > current[2]+1: # compare an unexplored neighbour's g score with the cost of reaching there through current node to see if it is the best established path so far
                        unexplored[n_idx][2] = current[2]+1 # update the g score
                        unexplored[n_idx][1] = current[0] # update the parent of that neighbour to the current node
                    else:
                        # No need to update - cost is the same or worse
                        continue
            
                # Newly discovered neighbour
                # Set the g value the f value parent to current
                neighbour_node=[]
                g_cost = current[2]+1
                f_cost = g_cost + heuristic(neighbour_coord, goal)  
                neighbour_node.append(neighbour_coord) # add the coordinate
                neighbour_node.append(current[0]) # add the parent
                neighbour_node.append(g_cost) # add the actual path cost
                neighbour_node.append(f_cost) # add the f cost
                unexplored.append(neighbour_node) # add the new node to the unexplored list
                

        if not unexplored: # all nodes have been explored and no possible path was found 
            success = False
            break


    if success:
        print_result(explored, current, start)
        

    else:
        print('0')

    return 

def print_result(explored, current, start):
    # This function simply prints the result by following the path back to the start state from the goal state
    # current: [ [y,x],[py,px],g,f ]
    path_distance = 1
    path=[]

    exp_coord_list = [item[0] for item in explored] # a list of coords of tiles explored

    while current[0] != start: # backtracking from goal to start
        path.append(tuple(current[0]))
        p_idx = exp_coord_list.index(current[1]) # retrive the parent index
        current = explored[p_idx] # follow the parent
        path_distance+=1

    path.append(tuple(start))
    print(path_distance)
    path.reverse()
    for coord in path:
        print(coord)
    
    return
    




def heuristic(current, goal):
    # This function returns a variation of the manhatten distance from a particular cell to the goal cell
    # y_1: represents the vertical coordinate of the current tile
    # x_1: " " horizontal coordinate " "
    # y_goal: represents the vertical coordinate of the goal tile
    # x_goal: represents the horizontal coordinate of the goal tile

    distance = 0 # distance to the goal tile
    y_1 = current[0]
    x_1 = current[1]
    y_goal = goal[0]
    x_goal = goal[1]

    y = y_1 - y_goal
    x = x_1 - x_goal

    distance = max(abs(y), abs(x), abs(x+y))

    return distance





def main():
    try:
        with open(sys.argv[1]) as file:
            data = json.load(file)
    except IndexError:
        print("usage: python3 -m search path/to/input.json", file=sys.stderr)
        sys.exit(1)
   
    a_star_search(data)
    n = data.get('n')
    board_dict = create_board_dict(data)
    
    #!Remove
    print_board(n,board_dict)

    
    
