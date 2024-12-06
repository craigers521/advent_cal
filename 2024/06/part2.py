from collections import Counter

P = complex

U = P(0, -1)
R = P(1,0)
D = P(0,1)
L = P(-1,0)

rotation = [U,R,D,L]

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


def run_loop(grid, start):
    pos = start
    index = 0
    dir = rotation[0]
    paths = set()
    while True:
        paths.add((pos, dir))
        if pos+dir not in grid: return False
        if grid[pos+dir] == "#":
            index += 1
            dir = rotation[index % 4]
        else:
            pos += dir
        if (pos, dir) in paths:
            return True



def find_loops(grid, start):
    count = 0
    for spot in grid:
        print(count)
        if grid[spot] != '.': continue
        grid[spot] = "#"
        if run_loop(grid, start):
            count += 1
        grid[spot] = '.'
    return count


def main():
    lines = read_input("input.txt")
    grid, start = make_grid(lines)
    ans = find_loops(grid, start)
    print(ans)


if __name__ == "__main__":
    main()