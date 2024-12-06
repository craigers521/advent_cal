from itertools import cycle
from collections import Counter

P = complex

U = P(0, -1)
R = P(1,0)
D = P(0,1)
L = P(-1,0)

turn = cycle([U, R, D, L])

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def make_grid(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            grid[P(x,y)] = val
            if val == "^": 
                start = P(x,y)
    return grid, start


def print_path(grid):
    for pos in grid:
        if pos.real == 0:
            print("\n")
        print(grid[pos], end='')
    return

def find_paths(grid, start):
    pos = start
    dir = next(turn)
    grid[pos] = '.'
    new_grid = grid.copy()
    new_grid[pos] = "X"
    while True:
        #print_path(new_grid)
        if pos+dir in grid and grid[pos+dir] == '.':
            pos = pos+dir
            new_grid[pos] = "X"
        elif pos+dir not in grid:
            return new_grid
        else:
            dir = next(turn)
            pos = pos+dir
            new_grid[pos] = "X"

def main():
    lines = read_input("input.txt")
    grid, start = make_grid(lines)
    path = find_paths(grid, start)
    #print_path(path)
    print(Counter(path.values())['X'])
    

if __name__ == "__main__":
    main()