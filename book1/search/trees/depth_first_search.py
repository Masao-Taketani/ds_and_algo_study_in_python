import copy

def search(data, start_pos_list):
    # to avoid changing values of the mutable object
    maze = copy.deepcopy(data)
    # initialize x, y, steps
    x, y, steps = start_pos_list
    # 1 indicates that it reached the goal point
    if maze[x][y] == 1:
        #print("It took {} step(s) to reach the goal.".format(steps))
        return

    # set tue position as "passed through"
    maze[x][y] = 2
    # do the depth search to the left
    if maze[x - 1][y] < 2:
        search(maze, [x - 1, y, steps + 1])
    # do the depth search to the right
    if maze[x + 1][y] < 2:
        search(maze, [x + 1, y, steps + 1])
    # do the depth search to the above
    if maze[x][y - 1] < 2:
        search(maze, [x, y - 1, steps + 1])
    # do the depth search to bottom
    if maze[x][y + 1] < 2:
        search(maze, [x, y + 1, steps + 1])
