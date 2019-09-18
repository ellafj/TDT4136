from .Map import Map_Obj
from .A1functions import initialize_node, euclidean, isGoal, reconstruct_path, generate_all_successors, initialize_child_node

def best_first_search(heuristic, state):
    closed = []
    open = []
    node0 = initialize_node(heuristic, state)
    open.append(node0)
    visited_nodes = {}

    while open:      # AGENDA-loop
        X = open.pop()
        closed.append(X)
        if isGoal(X.state):
            print('Found goal')
            return reconstruct_path(X, node0)
        children = generate_all_successors(X)
        for child in children:
            if child in visited_nodes:
                this_child = visited_nodes[child]
            else:
                this_child = initialize_child_node(X, child)
                visited_nodes[child] = this_child



