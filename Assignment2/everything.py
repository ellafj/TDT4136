import numpy as np
np.set_printoptions(threshold=np.inf, linewidth=300)
import pandas as pd
import time
from PIL import Image

class Map_Obj():
    path_cell = (1,2,3,4)
    wall_cell = -1
    starting_point = 'S'
    goal_point = 'G'
    def __init__(self, task=1):
        self.start_pos, self.goal_pos, self.end_goal_pos, self.path_to_map = self.fill_critical_positions(task)
        self.int_map, self.str_map = self.read_map(self.path_to_map)
        self.tmp_cell_value = self.get_cell_value(self.goal_pos)
        self.set_cell_value(self.start_pos, ' S ')
        self.set_cell_value(self.goal_pos, ' G ')
        self.tick_counter = 0
        #self.set_start_pos_str_marker(start_pos, self.str_map)
        #self.set_goal_pos_str_marker(goal_pos, self.str_map)

    def read_map(self, path):
        """
        Reads maps specified in path from file, converts them to a numpy array and a string array. Then replaces
        specific values in the string array with predefined values more suitable for printing.
        :param path: Path to .csv maps
        :return: the integer map and string map
        """
        # Read map from provided csv file
        df = pd.read_csv(path, index_col=None, header=None)#,error_bad_lines=False)
        # Convert pandas dataframe to numpy array
        data = df.values
        # Convert numpy array to string to make it more human readable
        data_str = data.astype(str)
        # Replace numeric values with more human readable symbols
        data_str[data_str == '-1'] = ' # '
        data_str[data_str == '1'] = ' . '
        data_str[data_str == '2'] = ' , '
        data_str[data_str == '3'] = ' : '
        data_str[data_str == '4'] = ' ; '
        return data, data_str

    def fill_critical_positions(self, task):
        """
        Fills the important positions for the current task. Given the task, the path to the correct map is set, and the
        start, goal and eventual end_goal positions are set.
        :param task: The task we are currently solving
        :return: Start position, Initial goal position, End goal position, path to map for current task.
        """
        if task == 1:
            start_pos = [27, 18]
            goal_pos = [40, 32]
            end_goal_pos = goal_pos
            path_to_map = 'Samfundet_map_1.csv'
        elif task == 2:
            start_pos = [40, 32]
            goal_pos = [8, 5]
            end_goal_pos = goal_pos
            path_to_map = 'Samfundet_map_1.csv'
        elif task == 3:
            start_pos = [28, 32]
            goal_pos = [6, 32]
            end_goal_pos = goal_pos
            path_to_map = 'Samfundet_map_2.csv'
        elif task == 4:
            start_pos = [28, 32]
            goal_pos = [6, 32]
            end_goal_pos = goal_pos
            path_to_map = 'Samfundet_map_Edgar_full.csv'
        elif task == 5:
            start_pos = [14, 18]
            goal_pos = [6, 36]
            end_goal_pos = [6, 7]
            path_to_map = 'Samfundet_map_2.csv'


        return start_pos, goal_pos, end_goal_pos, path_to_map

    def get_cell_value(self, pos):
        return self.int_map[pos[0], pos[1]]

    def get_goal_pos(self):
        return self.goal_pos

    def get_start_pos(self):
        return self.start_pos

    def get_end_goal_pos(self):
        return self.end_goal_pos

    def get_maps(self):
        # Return the map in both int and string format
        return self.int_map, self.str_map

    def move_goal_pos(self, pos):
        """
        Moves the goal position towards end_goal position. Moves the current goal position and replaces its previous
        position with the previous values for correct printing.
        :param pos: position to move current_goal to
        :return: nothing.
        """
        tmp_val = self.tmp_cell_value
        tmp_pos = self.goal_pos
        self.tmp_cell_value = self.get_cell_value(pos)
        self.goal_pos = [pos[0], pos[1]]
        self.replace_map_values(tmp_pos, tmp_val, self.goal_pos)

    def set_cell_value(self, pos, value, str_map = True):
        if str_map:
            self.str_map[pos[0], pos[1]] = value
        else:
            self.int_map[pos[0], pos[1]] = value

    def print_map(self, map_to_print):
        # For every column in provided map, print it
        for column in map_to_print:
            print(column)


    def pick_move(self):
        """
        A function used for moving the goal position. It moves the current goal position towards the end_goal position.
        :return: Next coordinates for the goal position.
        """
        if self.goal_pos[0] < self.end_goal_pos[0]:
            return [self.goal_pos[0]+1, self.goal_pos[1]]
        elif self.goal_pos[0] > self.end_goal_pos[0]:
            return [self.goal_pos[0]-1, self.goal_pos[1]]
        elif self.goal_pos[1] < self.end_goal_pos[1]:
            return [self.goal_pos[0], self.goal_pos[1]+1]
        else:
            return [self.goal_pos[0], self.goal_pos[1]-1]

    def replace_map_values(self, pos, value, goal_pos):
        """
        Replaces the values in the two maps at the coordinates provided with the values provided.
        :param pos: coordinates for where we want to change the values
        :param value: the value we want to change to
        :param goal_pos: The coordinate of the current goal
        :return: nothing.
        """
        if value == 1:
            str_value = ' . '
        elif value == 2:
            str_value = ' , '
        elif value == 3:
            str_value = ' : '
        elif value == 4:
            str_value = ' ; '
        else:
            str_value = str(value)
        self.int_map[pos[0]][pos[1]] = value
        self.str_map[pos[0]][pos[1]] = str_value
        self.str_map[goal_pos[0], goal_pos[1]] = ' G '


    def tick(self):
        """
        Moves the current goal position every 4th call if current goal position is not already at the end_goal position.
        :return: current goal position
        """
        # For every 4th call, actually do something
        if self.tick_counter % 4 == 0:
            # The end_goal_pos is not set
            if self.end_goal_pos is None:
                return self.goal_pos
            # The current goal is at the end_goal
            elif self.end_goal_pos == self.goal_pos:
                return self.goal_pos
            else:
                # Move current goal position
                move = self.pick_move()
                self.move_goal_pos(move)
                #print(self.goal_pos)
        self.tick_counter +=1

        return self.goal_pos


    def set_start_pos_str_marker(self, start_pos, map):
        # Attempt to set the start position on the map
        if self.int_map[start_pos[0]][start_pos[1]] == -1:
            self.print_map(self.str_map)
            print('The selected start position, '+str(start_pos) + ' is not a valid position on the current map.')
            exit()
        else:
            map[start_pos[0]][start_pos[1]] = ' S '

    def set_goal_pos_str_marker(self, goal_pos, map):
        # Attempt to set the goal position on the map
        if self.int_map[goal_pos[0]][goal_pos[1]] == -1:
            self.print_map(self.str_map)
            print('The selected goal position, '+ str(goal_pos) + ' is not a valid position on the current map.')
            exit()
        else:
            map[goal_pos[0]][goal_pos[1]] = ' G '

    def show_map(self, map=None):
        """
        A function used to draw the map as an image and show it.
        :param map: map to use
        :return: nothing.
        """
        # If a map is provided, set the goal and start positions
        if map is not None:
            self.set_start_pos_str_marker(self.start_pos, map)
            self.set_goal_pos_str_marker(self.goal_pos, map)
        # If no map is provided, use string_map
        else:
            map = self.str_map

        # Define width and height of image
        width = map.shape[1]
        height = map.shape[0]
        # Define scale of the image
        scale = 20
        # Create an all-yellow image
        image = Image.new('RGB', (width * scale, height * scale), (255, 255, 0))
        # Load image
        pixels = image.load()

        # Define what colors to give to different values of the string map (undefined values will remain yellow, this is
        # how the yellow path is painted)
        colors = {' # ': (255, 0, 0), ' . ': (215, 215, 215), ' , ': (166, 166, 166), ' : ': (96, 96, 96),
                  ' ; ': (36, 36, 36), ' S ': (255, 0, 255), ' G ': (0, 128, 255)}
        # Go through image and set pixel color for every position
        for y in range(height):
            for x in range(width):
                if map[y][x] not in colors: continue
                for i in range(scale):
                    for j in range(scale):
                        pixels[x * scale + i, y * scale + j] = colors[map[y][x]]
        # Show image
        image.show()

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
    def __str__(self):
        return "state is %s, parent is %s" % (self.state, self.parent)

def initialize_node(state0):
    n0 = search_node(state=state0)
    print(state0)
    n0.g = 0
    n0.h = euclidean(state0)
    n0.f = n0.g + n0.h
    return n0

def euclidean(state):
    pos = state
    print(pos)
    goal = [40, 32]#map.get_goal_pos()
    dist = ((goal[0]-pos[0])**2+(goal[1]-pos[1])**2)**0.5
    print(dist)
    return dist

def isGoal(state):
    x, y = state
    return tuple([40, 32]) == (x, y)

def reconstruct_path(current, board):
    totalPath = []
    while current.parent != board.start:
        current = current.parent
        totalPath.insert(0, current)
    totalPath.insert(0,current)
    return totalPath

def generate_all_successors(X):
    x, y = X.state
    df = pd.read_csv('Samfundet_map_1.csv', index_col=None, header=None)#,error_bad_lines=False)
    data = df.values
    print(data)
    (i,j) = data
    neigbours = [(1,0), (-1,0), (0,1), (0,-1)] # Maybe regular parenthis'?
    for x_dir, y_dir in neigbours:
        new_x = x + x_dir
        new_y = y + y_dir
        if (new_x < 0) or (new_y < 0) or (new_x >= i) or (new_y >= j):
            continue
        if map.get_cell_value((new_x, new_y)) != Map_Obj.wall_cell:
            yield (map, new_x, new_y)

def initialize_child_node(parent, node):
    state = node.state
    child = search_node(state=state, parent=parent)
    child.g = parent.g + 1 # Since 1 is the cost of moving from one point to another
    child.h = euclidean(child.state)
    child.f = child.g + child.f
    print('child: ', child)
    return child

def attach_and_eval(parent, child):
    child.parent = parent
    child.g = parent.g + 1 #Since cost of moving is 1
    child.h = euclidean(child.state)
    child.f = child.g + child.h

def sort_list(list):
    sorted_list = sorted(list, key=lambda x: x.f)
    return sorted_list

def propagate_path_improvements(node):
    for child in node.children:
        if node.g + 1 < child.g:
            child.parent = node
            child.g = node.g + 1
            child.f = child.g + child.h
            propagate_path_improvements(child)

def best_first_search(state):
    closed = []
    open = []
    node0 = initialize_node(state)
    print('node0', node0)
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
                print(child)
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

def main():
    map_obj = Map_Obj()
    state0 = [27, 18]#(map_obj, *map_obj.get_start_pos())
    print('state0', state0)

    output = best_first_search(state0)
    for coords in output:
        map_obj.set_cell_value(coords, "☺", str_map = True)

    map_obj.show_map()
    input()

main()

