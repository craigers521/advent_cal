from collections import deque

P = complex

U = P(0, -1)
R = P(1,0)
D = P(0,1)
L = P(-1,0)

dirs = [U,R,D,L]

def read_input(filename):
    with open(filename) as file:
        content = file.read()
    mapin, movesin = content.split("\n\n")
    maplines = [line for line in mapin.split()]
    moveslines = [line for line in movesin.split()]
    grid,start = make_grid(maplines)
    moves = combine_moves(moveslines)

    return grid, moves, start

def make_grid(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            grid[P(x,y)] = val
            if val =="@": start = P(x,y)
    return grid,start


def combine_moves(lines):
    moves = []
    for line in lines:
        for char in line:
            if char == "^":
                moves.append(U)
            if char == ">":
                moves.append(R)
            if char == "v":
                moves.append(D)
            if char == "<":
                moves.append(L)
    return moves


def move_robot(grid, moves, start):
    moveq = deque(moves)
    pos = start
    while moveq:
        step = moveq.popleft()
        if grid[pos+step] == "#":
            #print_grid(grid)
            continue
        if grid[pos+step] == ".":
            grid[pos] = "."
            grid[pos+step] = "@"
            pos = pos+step
            #print_grid(grid)
            continue
        if grid[pos+step] == "O":
            tempos = pos+step
            while grid[tempos] == "O":
                tempos = tempos+step
            if grid[tempos] == "#": continue
            if grid[tempos] == ".":
                grid[pos] = "."
                grid[pos+step] = "@"
                grid[tempos] = "O"
                pos = pos+step
                #print_grid(grid) 
    return grid


def print_grid(grid):
    for pos in grid:
        if pos.real == 0:
            print("")
        print(grid[pos], end='')
    print("")
    print("-"*20)
    print("\n")
    return


def find_gps(grid):
    total = 0
    for pos in grid:
        if grid[pos] == "O":
            total += (pos.imag*100)+pos.real
    return total


def main():
    grid, moves, start = read_input("input.txt")
    grid = move_robot(grid, moves, start)
    ans = find_gps(grid)
    print(ans)
    

if __name__ == "__main__":
    main()