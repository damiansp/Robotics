# Implement the function optimum_policy2D below.
#
# Given a car in grid with initial state <init>, compute and return the car's
# optimal path to the position specified in goal. The costs for each motion are
# defined in <cost>.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.
forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0]  # given in the form [row, col, direction]
                  # direction = 0: up, 1: left, 2: down, 3: right
goal = [2, 0]     # given in the form [row,col]
cost = [2, 1, 20] # cost has 3 values, corresponding to making
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------


def optimum_policy2D(grid, init, goal, cost):
    value = [[[999 for row in range(len(grid[0]))]
              for row in range(len(grid))],
             [[999 for row in range(len(grid[0]))]
              for row in range(len(grid))],
             [[999 for row in range(len(grid[0]))]
              for row in range(len(grid))],
             [[999 for row in range(len(grid[0]))]
              for row in range(len(grid))]]

    policy = [[[' ' for row in range(len(grid[0]))]
               for row in range(len(grid))],
              [[' ' for row in range(len(grid[0]))]
               for row in range(len(grid))],
              [[' ' for row in range(len(grid[0]))]
               for row in range(len(grid))],
              [[' ' for row in range(len(grid[0]))]
               for row in range(len(grid))]]
    
    policy2D = [[' ' for row in range(len(grid[0]))]
                for col in range(len(grid))]

    change = True

    while change:
        change = False

        # Go through all cells and calculate values
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for heading in range(4):
                    if goal[0] == x and goal[1] == y:
                        if value[heading][x][y] > 0:
                            change = True
                            value[heading][x][y] = 0
                            policy[heading][x][y] = '*'
                    elif grid[x][y] == 0:
                        # Calculate the 3 ways to propagate value
                        for i in range(3):
                            h2 = (heading + action[i]) % 4
                            x2 = x + forward[h2][0]
                            y2 = y + forward[h2][1]

                            if (x2 >= 0 and x2 < len(grid) and
                                y2 >= 0 and y2 < len(grid[0]) and
                                grid[x2][y2] == 0):
                                v2 = value[h2][x2][y2] + cost[i]
                                if v2 < value[heading][x][y]:
                                    value[heading][x][y] = v2
                                    policy[heading][x][y] = action_name[i]
                                    change = True
    # Indent level?
    x, y, heading = init

    policy2D[x][y] = policy[heading][x][y]
    while policy[heading][x][y] != '*':
        if policy[heading][x][y] == '#':
            h2 = heading
        elif policy[heading][x][y] == 'R':
            h2 = (heading - 1) % 4
        elif policy[heading][x][y] == 'L':
            h2 = (heading + 1) % 4

        x = x + forward[h2][0]
        y = y + forward[h2][1]
        heading = h2
        policy2D[x][y] = policy[heading][x][y]

    for row in policy2D:
        print row
        
    return policy2D
        

optimum_policy2D(grid, init, goal, cost)
