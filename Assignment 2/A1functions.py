from .Map import Map_Obj

class search_node:
    """
    • state - an object describing a state of the search process
    • g - cost of getting to this node
    • h - estimated cost to goal
    • f - estimated total cost of a solution path going through this node; f = g + h
    • status - open or closed
    • parent - pointer to best parent node
    • kids - list of all successor nodes, whether or not this node is currently their best parent.
    """
    def __init__(self, state=None, g=None, h=None, f=None, status=None, parent=None, children=None):
        self.state = state
        self.g = g
        self.h = h
        self.f = f
        self.status = status
        self.parent = parent
        if children:
            self.children = children
        else:
            self.children = []

def initialize_node(heuristic, state0):
    n0 = search_node(state=state0)
    n0.g = 0
    n0.h = heuristic(state0)
    n0.f = n0.g + n0.h
    return n0

def euclidean(state):
    map, *pos = state
    goal = map.get_goal_pos()
    return ((goal[0]-pos[0])**2+(goal[1]-pos[1])**2)**0.5

def isGoal(state):
    map, x, y = state
    return tuple(map.get_goal_pos()) == (x, y)

def reconstruct_path(current, board):
    totalPath = []
    while current.parent != board.start:
        current = current.parent
        totalPath.insert(0, current)
    totalPath.insert(0,current)
    return totalPath

def generate_all_successors(X):
    map, x, y = X.state
    (i,j) = map.int_map.shape
    neigbours = [(1,0), (-1,0), (0,1), (0,-1)] # Maybe regular parenthis'?
    for x_dir, y_dir in neigbours:
        new_x = x + x_dir
        new_y = y + y_dir
        if (new_x < 0) or (new_y < 0) or (new_x >= i) or (new_y >= j):
            continue
        if map.get_cell_value((new_x, new_y)) != Map_Obj.wall_cell:
            yield (map, new_x, new_y)

def initialize_child_node(parent, node):
    child = search_node(state=node.state, parent=parent)
    child.g = parent.g + 1 # Since 1 is the cost of moving from one point to another
    child.h = euclidean(child.state)
    child.f = child.g + child.f
    return child
