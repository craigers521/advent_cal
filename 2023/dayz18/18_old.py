from shapely.geometry import Polygon,Point

P = complex
U = P(0,-1)
D = P(0,1)
L = P(-1,0)
R = P(1,0)

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def parse_lines(lines):
    plan = [line.split() for line in lines]
    for line in plan:
        line[1] = int(line[1])
    return plan

def dig_trench(plan):
    pos = P(0,0)
    grid = {}
    grid[pos] = plan[0][2]
    for instr in plan:
        ddir,dlen,color = instr[0],instr[1],instr[2]
        if ddir == 'R': ddir = R
        if ddir == 'L': ddir = L
        if ddir == 'U': ddir = U
        if ddir == 'D': ddir = D 
        for _ in range(dlen):
            pos += ddir
            grid[pos] = color
    return grid 

            
def find_area(grid):
    a1,a2 = 0,0
    xs = []
    ys = []
    for node in grid.keys():
        xs.append(node.real)
        ys.append(node.imag)
    for i in range(len(xs)-1):
        a1 += xs[i]*ys[i+1]
        a2 += ys[i]*xs[i+1]
    return abs(a1-a2)//2


def print_trench(grid):
    for y in range(224):
        for x in range(389):
            if P(x,y) in grid:
                print('#', end='')
            else: 
                print('.', end='')
        print('\n')

def print_grid(grid):
    for y in range(224):
        for x in range(389):
            print(grid[P(x,y)], end='')
        print('\n')


def make_poly(grid):
    coords = []
    for node in grid.keys():
        coords.append((node.real, node.imag))
    poly = Polygon(coords)
    return poly


def fill_grid(grid):
    xs = []
    ys = []
    for node in grid.keys():
        xs.append(int(node.real))
        ys.append(int(node.imag))
    cols = max(xs)
    rows = max(ys)
    for y in range(rows+1):
        digstart = False
        digend = False
        dignew = False
        for x in range(cols+1):
            if digend:
                continue
            if P(x,y) in grid and not digstart:
                digstart = True
            elif P(x,y) not in grid and digstart:
                grid[P(x,y)] = '#'
                dignew = True
            elif P(x,y) in grid and dignew:
                digend = True
    return


def make_grid(trench):
    grid = {}
    xs = []
    ys = []
    for node in trench.keys():
        xs.append(int(node.real))
        ys.append(int(node.imag))
    cols = max(xs)
    rows = max(ys)
    for y in range(rows+1):
        for x in range(cols+1):
            if P(x,y) in trench:
                grid[P(x,y)] = '#'
            else:
                grid[P(x,y)] = '.'
    return grid

def in_poly(trench, grid):
    tiles = 0
    for point in grid:
        if point not in trench:
            if ray_cast(point,trench,grid)%2 == 1:
                tiles += 1
                grid[point] = '#'
    return tiles
        

def ray_cast(point,trench,grid):
    edges = 0
    pos = point+P(1,0)
    while pos in grid:
        if pos in trench:
                edges += 1
        pos = pos+P(1,0)
    return edges   
                

def main():
    lines = read_input("input.txt")
    plan = parse_lines(lines)
    trench = dig_trench(plan)
    #print_grid(grid)
    #area = find_area(grid)
    #poly = make_poly(grid)
    #print(poly.area)
    #fill_grid(grid)
    grid = make_grid(trench)
    tiles = in_poly(trench, grid)
    print_grid(grid)
    print(tiles+len(trench))

    

if __name__ == "__main__":
    main()