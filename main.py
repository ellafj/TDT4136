## Based on pseudocode from Wikipedia and the given resource about A*
from .Map  import Map_Obj

obj = Map_Obj()



def reconstruct_path(cameFrom, current, board):
    totalPath = []
    while current.cameFrom.__ne__(board.start):
        current = current.cameFrom
        totalPath.insert(0, current)
    totalPath.insert(0,current)
    return totalPath

