from collections import deque

P = complex

U = P(0, -1)
R = P(1,0)
D = P(0,1)
L = P(-1,0)

dirs = [U,R,D,L]

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def make_grid(lines):
    grid = {}
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            grid[P(x,y)] = val
    return grid


def make_regions(grid):
    master_seen = set()
    regions = []
    for point in grid:
        if point in master_seen: continue
        q = deque([point])
        seen = {point}
        while q:
            pos = q.popleft()
            for dir in dirs:
                step = pos+dir
                if step not in grid: continue
                if grid[step] != grid[pos]: continue
                if step in seen: continue
                seen.add(step)
                q.append(step)
        master_seen.update(seen)
        area = len(seen)
        sides = find_sides(seen)
        regions.append((area, sides))
        #print(grid[pos], sides, end="\n")
    return regions


def find_sides(region):
    NW = P(-1,-1)
    NE = P(1,-1)
    SW = P(-1,1)
    SE = P(1,1)
    up, down, left, right = (set() for _ in range(4))
    sides = 0
    for point in region:
        if point+U not in region: up.add(point)
        if point+D not in region: down.add(point)
        if point+R not in region: right.add(point)
        if point+L not in region: left.add(point)
    for point in up:
        if point in left: 
            sides += 1
        if point in right: 
            sides += 1
        if point+NW in right and point not in left: 
            sides += 1
        if point+NE in left and point not in right: 
            sides += 1
    for point in down:
        if point in left: 
            sides += 1
        if point in right: 
            sides += 1
        if point+SW in right and point not in left: 
            sides += 1
        if point+SE in left and point not in right: 
            sides += 1
    return sides


def find_price(regions):
    total = 0
    for x,y in regions:
        total += x*y
    return total


def main():
    lines = read_input("input.txt")
    grid = make_grid(lines)
    regions = make_regions(grid)
    ans = find_price(regions)
    print(ans)

if __name__ == "__main__":
    main()