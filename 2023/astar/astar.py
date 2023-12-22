from heapq import heappop,heappush

P = complex
UP = -1j
DOWN = 1j
LEFT = -1
RIGHT = 1

class Node:
    def __init__(self, parent, pos):
        self.parent = parent
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        self.pos == other.pos
    
    def __lt__(self, other):
        self.f < other.f
    
    def __hash__(self):
        return hash(self.pos)


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def make_grid(lines):
    grid = set()
    walls = set()
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            if val == 'S': start = P(x,y)
            elif val == '.': grid.add(P(x,y))
            elif val == '#': walls.add(P(x,y))
            elif val == 'T': 
                target = P(x,y)
                grid.add(P(x,y))
    return grid, walls, start, target


def astar(grid,start,target):
    start_node = Node(None,start)
    end_node = Node(None,target)
    open = [start_node]
    closed = set()

    while len(open) > 0:
        flag = False
        current_node = heappop(open)
        closed.add(current_node)
        
        if current_node == end_node:
            path = []
            current = current_node
            while current.parent is not None:
                path.append(current.pos)
                current = current.parent
            return path[::-1]
        
        children = []
        for dpos in (UP,DOWN,LEFT,RIGHT):
            npos = dpos+current_node.pos
            if npos in grid:
                child_node = Node(current_node, npos)
                children.append(child_node)
        
        for child in children:
            if child in closed:
                continue
            child.g = current_node.g+1
            child.h = calc_h(child.pos, end_node.pos)
            child.f = child.g+child.h

            for n in open:
                if n.pos == child.pos and child.g > n.g:
                    flag = True
            if flag:
                flag = False
                continue
            heappush(open, child)

    return None


def calc_h(pos1, pos2):
    dist = pos2-pos1
    h = int((dist.real**2)+(dist.imag**2))
    return h




def main():
    lines = read_input("test1.txt")
    grid,walls,start,target = make_grid(lines)
    path = astar(grid,start,target)
    print(path)

    
    

if __name__ == "__main__":
    main()