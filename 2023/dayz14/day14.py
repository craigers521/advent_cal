from collections import defaultdict

P = complex
north = P(0,-1)
west = P(-1,0)
south = P(0,1)
east = P(1,0)

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
            if val != '.':
                grid[P(x,y)] = val
    return rows,cols,grid

def find_weight(rows,cols,dish):
    move_north(dish,rows,cols)
    print_dish(dish,rows,cols)
    weight = calc_load(dish,rows,cols)
    return weight


def move_north(dish,rows,cols):
    round_rocks = {k:v for (k,v) in dish.items() if dish[k] == 'O'}
    for r in range(rows):
        for c in range(cols):
            key = P(c,r)
            if key in round_rocks: rock = dish.pop(key)
            else: continue
            while key not in dish and key.imag >= 0:
                key += north
            key += P(0,1)
            dish[key] = rock
    return

def move_west(dish,rows,cols):
    round_rocks = {k:v for (k,v) in dish.items() if dish[k] == 'O'}
    for c in range(cols):
        for r in range(rows):
            key = P(c,r)
            if key in round_rocks: rock = dish.pop(key)
            else: continue
            while key not in dish and key.real >= 0:
                key += west
            key += P(1,0)
            dish[key] = rock
    return

def move_south(dish,rows,cols):
    round_rocks = {k:v for (k,v) in dish.items() if dish[k] == 'O'}
    for r in range(rows,-1,-1):
        for c in range(cols):
            key=P(c,r)
            if key in round_rocks: rock = dish.pop(key)
            else: continue
            while key not in dish and key.imag < rows:
                key += south
            key += P(0,-1)
            dish[key] = rock
    return

def move_east(dish,rows,cols):
    round_rocks = {k:v for (k,v) in dish.items() if dish[k] == 'O'}
    for c in range(cols,-1,-1):
        for r in range(rows):
            key=P(c,r)
            if key in round_rocks: rock = dish.pop(key)
            else: continue
            while key not in dish and key.real < cols:
                key += east
            key += P(-1,0)
            dish[key] = rock
    return

def calc_load(dish,rows,cols):
    weight = 0
    multiplier = rows
    for r in range(rows):
        counter = 0
        for x in range(cols):
            key = P(x,r)
            if key in dish and dish[key] == 'O':
                counter += 1
        weight += counter*multiplier
        multiplier -= 1
    return weight


def print_dish(dish,rows,cols):
    print('_'*50)
    for y in range(rows):
        for x in range(cols):
            key = P(x,y)
            if key in dish:
                print(dish[key], end='')
            else:
                print('.', end='')
        print('\n')
    return

def cycle_dish(rows,cols,dish,cycle):
    weights = defaultdict(int)
    while cycle > 0:
        move_north(dish,rows,cols)
        #print_dish(dish,rows,cols)
        move_west(dish,rows,cols)
        #print_dish(dish,rows,cols)
        move_south(dish,rows,cols)
        #print_dish(dish,rows,cols)
        move_east(dish,rows,cols)
        #print_dish(dish,rows,cols)
        test = calc_load(dish,rows,cols)
        weights[test] += 1
        #print(f"{200-cycle}: {test}")
        cycle -=1
    for key in weights:
        if weights[key] > 1:
            print(f"{key} : {weights[key]}")
    return
        
        


def main():
    lines = read_input("input.txt")
    rows,cols,dish = make_grid(lines)
    #p1 = find_weight(rows,cols,dish)
    #print(p1)
    cycle_dish(rows,cols,dish,cycle=1000)

    

if __name__ == "__main__":
    main()