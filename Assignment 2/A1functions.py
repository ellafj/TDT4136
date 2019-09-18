## Heuristic function
def euclidean(state):
    map_, *pos = state
    goal = map_.get_goal_pos()
    return ((goal[0]-pos[0])**2+(goal[1]-pos[1])**2)**0.5
