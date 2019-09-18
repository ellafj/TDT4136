from .Map import Map_Obj

def euclidean(state):
    map_, *pos = state
    goal = map_.get_goal_pos()
    return ((goal[0]-pos[0])**2+(goal[1]-pos[1])**2)**0.5

def isGoal(state):
    map_, x, y = state
    return tuple(map_.get_goal_pos()) == (x, y)

def reconstruct_path(current, board):
    totalPath = []
    while current.parent != board.start:
        current = current.parent
        totalPath.insert(0, current)
    totalPath.insert(0,current)
    return totalPath

def generate_all_successors(X):
    map_, x, y = X.state
    (i,j) = map_.int_map.shape
    neigbours = [(1,0), (-1,0), (0,1), (0,-1)] # Maybe regular parenthis'?
    for dx, dy in neigbours:
        new_x = x + dx
        new_y = y + dy


def successors_gen(state):
    '''
    Generator function which yields all successors for a given state.
    '''
    map_, x, y = state
    (w, h) = map_.int_map.shape

    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        x_ = x + dx
        y_ = y + dy

        if (x_ < 0) or (x_ >= w) or (y_ < 0) or (y_ >= h):
            continue

        if map_.get_cell_value((x + dx, y + dy)) != Map_Obj.OBSTACLE_CELL:
            yield (map_, x + dx, y + dy)
