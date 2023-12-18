import heapq
from collections import defaultdict

P = complex
UP = P(0,-1)
DOWN = P(0,1)
LEFT = P(-1,0)
RIGHT = P(1,0)

class Node:
    def __init__(self,loss,pos,pdir,steps):
        self.loss = loss
        self.pos = pos
        self.pdir = pdir
        self.steps = steps
        self.key = (self.pos, self.pdir, self.steps)

    def __lt__(self,other):
        return (self.loss, self.steps)<(other.loss, other.steps)


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def make_grid(lines):
    rows = len(lines)
    cols = len(lines[0])
    grid = {}
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
                grid[P(x,y)] = int(val)
    end = P(cols-1,rows-1)
    return grid,end

def find_path(grid,end):
    shadow_grid = defaultdict(int)
    seen = set()
    Q = [Node(0, P(0,0), DOWN, 0), Node(0, P(0,0), RIGHT, 0)]
    while Q:
        node = heapq.heappop(Q)
        if node.key in seen:
            continue
        seen.add(node.key)
        loss,pos,pdir,steps = node.loss, node.pos, node.pdir, node.steps
        shadow_grid[pos] = pdir
        if pos == end and steps >= 4:
            return loss,shadow_grid
        if steps < 10 and pos+pdir in grid:
            heapq.heappush(Q, Node(loss+grid[pos+pdir], pos+pdir, pdir, steps+1))
        if pdir in (UP, DOWN) and steps >= 4:
            if pos+LEFT in grid:
                heapq.heappush(Q, Node(loss+grid[pos+LEFT], pos+LEFT, LEFT, 1))
            if pos+RIGHT in grid:
                heapq.heappush(Q, Node(loss+grid[pos+RIGHT], pos+RIGHT, RIGHT, 1))
        elif pdir in (LEFT, RIGHT) and steps >=4:
            if pos+UP in grid:
                heapq.heappush(Q, Node(loss+grid[pos+UP], pos+UP, UP, 1))
            if pos+DOWN in grid:
                heapq.heappush(Q, Node(loss+grid[pos+DOWN], pos+DOWN, DOWN, 1))
        #print_seen(shadow_grid)


def print_seen(nodes):
    for y in range(13):
        for x in range(13):
            pos = P(x,y)
            if pos in nodes:
                if nodes[pos] == UP: print('^', end='')
                if nodes[pos] == DOWN: print('v', end='')
                if nodes[pos] == LEFT: print('<', end='')
                if nodes[pos] == RIGHT: print('>', end='')
            else: print('O', end='')
        print('\n')
    print('_'*30)
                

def main():
    lines = read_input("sample.txt")
    grid,end = make_grid(lines)
    p1,shadow_grid = find_path(grid,end)
    print_seen(shadow_grid)
    print(p1)
    

if __name__ == "__main__":
    main()