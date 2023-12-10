from shapely.geometry import Point,Polygon

P = complex
ptypes = {
    "|": [P(0,-1), P(0,1)], #up or down
    "-": [P(-1,0), P(1,0)], #left or right
    "L": [P(0,-1), P(1,0)], #up or right
    "J": [P(0,-1), P(-1,0)], #up or left
    "7": [P(0,1), P(-1,0)], #down or left
    "F": [P(0,1), P(1,0)], #down or right
    "S": [P(0,1), P(1,0)] # change S pipe to match behavior
}

def char_replace(input):
    if input == "|": return "║"
    if input == "-": return "═"
    if input == "L": return "╚"
    if input == "J": return "╝"
    if input == "7": return "╗"
    if input == "F": return "╔"
    return input


def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def make_grid(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
              grid[P(x,y)] = val
    return grid


def next_hop(current, grid, ploop):
    for d in ptypes[grid[current]]:
        if d+current not in ploop:
            return d+current
        if grid[d+current] == 'S' and len(ploop) > 2:
            return d+current
    return


def find_loop(grid):
    ploop = []
    start = [k for k,v in grid.items() if v == 'S']
    ploop.append(start[0])
    pos = next_hop(start[0], grid, ploop)
    while grid[pos] != 'S':
        ploop.append(pos)
        pos = next_hop(pos, grid, ploop)
    return ploop


def print_path(ploop, grid):
    for pos in grid:
        if pos.real == 0:
          print("\n")
        if pos in ploop:
            char = char_replace(grid[pos])
            print(char, end ='')
        else: print('.', end='')
        

def in_poly(ploop, grid):
    tiles = 0
    for point in grid:
        p = grid[point]
        if grid[point] == '.':
            if ray_cast(point,ploop,grid)%2 == 1:
                tiles += 1
    return tiles
        

def ray_cast(point,ploop,grid):
    edges = 0
    pos = point+P(1,0)
    while pos in grid:
        char = grid[pos]
        if pos in ploop:
            if grid[pos] != "-":
                edges += 1
            else: return 0
        pos = pos+P(1,0)
    return edges


def make_poly(ploop):
    coords = []
    for point in ploop:
        coords.append((point.real,point.imag))
    poly = Polygon(coords)
    return poly


def find_tiles(grid, poly):
    tiles = 0
    for point in grid:
        p = Point(point.real, point.imag)
        if poly.contains(p):
            tiles +=1
    return tiles



def main():
    lines = read_input("input.txt")
    grid = make_grid(lines)
    ploop = find_loop(grid)
    print(len(ploop)//2)
    #print_path(ploop, grid)
    #p2 = in_poly(ploop,grid)
    poly = make_poly(ploop)
    p2 = find_tiles(grid, poly)
    print(p2)

    

if __name__ == "__main__":
    main()