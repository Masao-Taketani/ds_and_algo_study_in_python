import copy

def search(data, start_pos_list):
    # to avoid changing values of the mutable object
    maze = copy.deepcopy(data)
    pos = []
    pos.append(start_pos_list)

    while len(pos) > 0:
        x, y, steps = pos.pop(0)
        # 1 indicates that it reached the goal point
        if maze[x][y] == 1:
            #print("It took {} step(s) to reach the goal.".format(steps))
            break

        # set tue position as "passed through"
        maze[x][y] = 2
        # if it has't pass through the left point, add it to the list
        # while setting up the steps + 1
        if maze[x - 1][y] < 2:
            pos.append([x - 1, y, steps + 1])
        # do the same search for the right point
        if maze[x + 1][y] < 2:
            pos.append([x + 1, y, steps + 1])
        # do the same search for the above point
        if maze[x][y - 1] < 2:
            pos.append([x, y - 1, steps + 1])
        # do the same search for the bottom point
        if maze[x][y + 1] < 2:
            pos.append([x, y + 1, steps + 1])
