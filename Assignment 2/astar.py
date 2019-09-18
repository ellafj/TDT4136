from .Map import Map_Obj
import A1functions

a = euclidean(state)

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


def best_first_search(heuristic, state):
    closed = []
    open = []
    node = initialize_node(heuristic, state)
    open.append(node)

    while open:      # AGENDA-loop
        X = open.pop()
        closed.append(X)


def reconstruct_path(cameFrom, current, board):
    totalPath = []
    while current.cameFrom.__ne__(board.start):
        current = current.cameFrom
        totalPath.insert(0, current)
    totalPath.insert(0,current)
    return totalPath
