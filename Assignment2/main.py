from .Map import Map_Obj
from .astar import best_first_search

def main():
    map_obj = Map_Obj()
    state0 = (map_obj, *map_obj.get_start_pos())

    output = best_first_search(state0)
    for coords in output:
        map_obj.set_cell_value(coords, "☺", str_map = True)

    map_obj.show_map()
    input()

main()



