from .Map import Map_Obj
from .A1functions import (initialize_node, euclidean, isGoal, reconstruct_path, generate_all_successors, initialize_child_node,
                          attach_and_eval, sort_list, propagate_path_improvements)

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
            # Making child into node
            if child in visited_nodes:
                child_node = visited_nodes[child]
            else:
                child_node = initialize_child_node(X, child)
                visited_nodes[child] = child_node
            (X.children).append(child_node)
            if child_node not in open and child_node not in closed:
                attach_and_eval(X, child_node)
                open.append(child_node)
                open = sort_list(open)
            elif X.g + 1 < child_node.g:
                attach_and_eval(X, child_node)
                if child_node in closed:
                    propagate_path_improvements(child_node)



