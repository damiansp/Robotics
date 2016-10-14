# Implement a function compute_value which returns a grid of values. The value
# of a cell is the minimum number of moves required to get from the cell to the
# goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
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

def compute_value(grid, goal, cost):
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
        
    for row in value:
        print row
    return value


compute_value(grid, goal, cost)
