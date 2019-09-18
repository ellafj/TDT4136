from .Map  import Map_Obj

class Node:
    """
    • state - an object describing a state of the search process
    • g - cost of getting to this node
    • h - estimated cost to goal
    • f - estimated total cost of a solution path going through this node; f = g + h
    • status - open or closed
    • parent - pointer to best parent node
    • kids - list of all successor nodes, whether or not this node is currently their best parent.
    """
    def search_node(self, state=None, g=None, h=None, f=None, status=None, parent=None, children=None):
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

def initialize_node():
    n0 = Node()
    n0.g = 0
    n0.h =

def best_first_search():
    closed = []
    open = []
    node = initialize_node()

def reconstruct_path(cameFrom, current, board):
    totalPath = []
    while current.cameFrom.__ne__(board.start):
        current = current.cameFrom
        totalPath.insert(0, current)
    totalPath.insert(0,current)
    return totalPath
