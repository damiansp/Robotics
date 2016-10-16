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
    fringe = [[0] + init] # [min_cost, x (row), y (col), heading]
    visited = fringe
    values = [[999 for col in range(len(grid[0]))] for row in range(len(grid))]

    for i in range(len(values)):
        for j in range(len(values[0])):
            # if barrier, assign 999
            if grid[i][j] == 1:
                values[i][j] = 999
            else:
                # split cell into four parts (1 for each heading) and
                # initialize all to 999
                values[i][j] = [999] * 4
        
    while len(fringe) > 0:
        state = fringe.pop()
        x, y, h = state[1:]

        # expand the fringe
        for a in range(len(action)): # R: -1, S: 0, L: 1
            move = forward[(h + action[a]) % 4]
            x2, y2, h2 = x + move[0], y + move[1], (h + a) % 4
            # Validate position
            if (x2 >= 0 and x2 < len(grid) and
                y2 >= 0 and y2 < len(grid[0]) and
                grid[x2][y2] == 0):
                reachable_state = [state[0] + cost[a], x2, y2, h2]
                # append reachable state if state has not been visited before
                # OR if new score is better than existing score
                already_visited = False
                for v in range(len(visited)):
                    if visited[v][1:] == reachable_state[1:]:
                        already_visited = True
                        if reachable_state[0] < visited[v][0]:
                            # replace
                            visited[v] = reachable_state
                            # update in fringe with new score
                            for s in range(len(fringe)):
                if not already_visited:
                    visited.append(reachable_state)
                    fringe.append(reachable_state)
                    fringe.sort()
                    fringe.reverse()
                    print fringe

    for row in values:
        print row


    # From the initial positionExpand the fringe
    #return policy2D
        

optimum_policy2D(grid, init, goal, cost)
