## Based on pseudocode from Wikipedia and the given resource about A*
from .Map  import Map_Obj

obj = Map_Obj()

class Node:
    def __init__(self, state=None, f=None, g=None, h=None, parent=None, child=None):
        self.state = state
        self.f = f
        self.g = g
        self.h = h
        self.parent = parent
        if child:
            self.child = child
        else:
            self.child = []

def reconstruct_path(cameFrom, current, board):
    totalPath = []
    while current.cameFrom.__ne__(board.start):
        current = current.cameFrom
        totalPath.insert(0, current)
    totalPath.insert(0,current)
    return totalPath

