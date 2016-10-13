# Define a function, search() that returns a grid showing the ordering of 
# visits to each state (-1 if state not visited).
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

    path = visited[len(visited) - 1]
    print path
    return expand

print search(grid, init, goal, cost)
