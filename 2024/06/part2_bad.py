from collections import Counter, deque

P = complex

U = P(0, -1)
R = P(1,0)
D = P(0,1)
L = P(-1,0)

Q = deque([U, R, D, L])

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

def char_replace(input):
    if input == U: return "↑"
    if input == D: return "↓"
    if input == R: return "→"
    if input == L: return "←"
    return input

def print_path(grid):
    for pos in grid:
        if pos.real == 0:
            print("\n")
        print(char_replace(grid[pos]), end='')
    print("\n")
    print("-"*15)
    print("\n")
    return

def find_paths(grid, start):
    pos = start
    dir = Q[0]
    grid[pos] = dir
    count = 0
    while True:
        #print_path(grid)
        if pos+dir in grid and grid[pos+dir] == '.':
            temp_dir = Q[1]
            if grid[pos+temp_dir] in Q:
                count += 1
        if pos+dir in grid and grid[pos+dir] != '#':
            pos = pos+dir
            grid[pos] = dir
        elif pos+dir not in grid:
            return count
        else:
            Q.rotate(-1)
            dir = Q[0]
            pos = pos+dir
            grid[pos] = dir

def main():
    lines = read_input("input.txt")
    grid, start = make_grid(lines)
    ans = find_paths(grid, start)
    print(ans)


if __name__ == "__main__":
    main()