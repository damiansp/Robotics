# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,up, and down motions.
# '*' should mark the goal cell.
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space (wall/barrier)

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1 # per movement

# Moves
delta = [[-1,  0], # go up
         [ 0, -1], # go left
         [ 1,  0], # go down
         [ 0,  1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid, init, goal, cost):
    state = init           # current position
    visited = []           # track explored states
    fringe = [[0] + init]  # track reached, but not expanded states (to expand)

    # Init expand grid to size = grid.size and all vals to -1
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand[0][0] = 0
    order_visited = 1

    while state[1:] != goal:
        if len(fringe) == 0:
            return 'fail'
        
        # update state to fringe state with minimum cost (g-value)
        state_index = 0
        min_g = fringe[state_index][0]
                
        for s in range(len(fringe)):
            if fringe[s][0] < min_g:
                state_index = s
                min_g = fringe[s][0]

        # remove state from fringe
        state = fringe[state_index]
        del fringe[state_index]
        
        # expand state
        for move in delta:
            possible_new_state = [state[1] + move[0], state[2] + move[1]]
            # check if barrier or out of bounds
            if (possible_new_state[0] >= 0
                and possible_new_state[0] < len(grid)
                and possible_new_state[1] >= 0
                and possible_new_state[1] < len(grid[0])
                and grid[possible_new_state[0]][possible_new_state[1]] != 1):

                # check if already explored
                state_visited = False
                for v in visited:
                    if v[1:] == possible_new_state:
                        state_visited = True

                # if not visited add to fringe
                if not state_visited:
                    # add cost to state
                    fringe += [[state[0] + cost] + possible_new_state]
                    expand[possible_new_state[0]][possible_new_state[1]] = \
                        order_visited
                    order_visited += 1

        # add state to visited
        visited += [state]

    # Init path grid to same size, and all vals to n_row * n_col (the max
    # possible score for any cell)
    path = [[len(grid) * len(grid[0]) for row in range(len(grid[0]))]
            for col in range(len(grid))]
    # Populate pathe with scores from visited
    for v in visited:
        path[v[1]][v[2]] = v[0]

    # Starting at goal, back trace by moving to whichever reachable cell has
    # the min value
    backtrace = goal
    path[goal[0]][goal[1]] = '*'

    while backtrace != init:
        # check all possible moves, determine best move (= cell with min val)
        best_val = path[backtrace[0]][backtrace[1]]
        best_move = ''
    
        for move in delta:
            loc = [backtrace[0] + move[0], backtrace[1] + move[1]]
            # make sure move in bounds and not an obstacle
            if (loc[0] >= 0 and loc[0] < len(grid)
                and loc[1] >= 0 and loc[1] < len(grid[0])
                and grid[loc[0]][loc[1]] != 1):
                if path[loc[0]][loc[1]] < best_val:
                    best_val = path[loc[0]][loc[1]]
                    best_move = move

        backtrace[0] += best_move[0]
        backtrace[1] += best_move[1]
        # update path map: since we are backtracing, arrow direction is
        # opposite of backtrace's best_move
        for m in range(len(delta)):
            if delta[m] == best_move:
                path[backtrace[0]][backtrace[1]] = delta_name[(m + 2) % 4]
            
    # Replace all non-arrow values with ' '
    for r in range(len(path)):
        for c in range(len(path[0])):
            if isinstance(path[r][c], int):
                path[r][c] = ' '

    return path

print search(grid, init, goal, cost)
