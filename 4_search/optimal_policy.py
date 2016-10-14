# Function optimum_policy returns a grid which shows the optimum policy for
# robot motion. This means there should be an optimum direction associated with
# each navigable cell from which the goal can be reached.
#
# Unnavigable cells as well as cells from which the goal cannot be reached
# should have a string  containing a single space (' '). The goal cell should
# have '*'.
# ----------


grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1,  0], # go up
         [ 0, -1], # go left
         [ 1,  0], # go down
         [ 0,  1]] # go right
delta_name = ['^', '<', 'v', '>']

def optimum_policy(grid, goal, cost):
    # Init value grid w all values = 99
    value = [[99 for i in range(len(grid[0]))] for j in range(len(grid))]
    x, y = goal
    score = 0
    fringe = [[score] + goal] # set of states with moves yet to be explored
    
    value[x][y] = score

    while len(fringe) > 0:
        # pick next fringe state
        state = fringe.pop()
        x, y = state[1:]

        # set score to state's score + cost
        score = state[0] + 1

        # for each reachable state (in bounds and not barrier)
        for move in delta:
            x2, y2 = x + move[0], y + move[1]
            # check that in-bounds
            if (x2 >= 0 and x2 < len(grid) and
                y2 >= 0 and y2 < len(grid[0]) and # check if barrier
                grid[x2][y2] != 1):

                # if state is NEW (val == 99) and assign value and...
                if value[x2][y2] == 99:
                    value[x2][y2] = score
                    # add to fringe
                    fringe.append([score, x2, y2])
                    fringe.sort()
                    fringe.reverse()

    # Use value to create policy. For any grid cell point to min neighbor
    policy = [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]
    policy[goal[0]][goal[1]] = '*'

    # For each cell in policy:
    for x in range(len(policy)):
        for y in range(len(policy[0])):
            # If cell is reachable and not a barrier
            if value[x][y] != 99:
                best_value = value[x][y]
                # For all neighbors
                for move in range(len(delta)):
                    x2, y2 = x + delta[move][0], y + delta[move][1]
                    if (x2 >= 0 and x2 < len(grid) and
                        y2 >= 0 and y2 < len(grid[0])):
                        if value[x2][y2] < best_value:
                            # determine the one with the min value
                            best_value = value[x2][y2]
                            # assign the appropriate arrow marker
                            policy[x][y] = delta_name[move]
                


        
    for row in policy:
        print row
    return policy


optimum_policy(grid, goal, cost)
