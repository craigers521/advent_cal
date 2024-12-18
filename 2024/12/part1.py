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
        perimeter = find_perimeter(seen, grid)
        regions.append((area, perimeter))
    return regions


def find_perimeter(points, grid):
    perimeter = 0
    for point in points:
        for dir in dirs:
            step = point+dir
            if step not in grid: 
                perimeter += 1
                continue
            if grid[step] != grid[point]:
                perimeter += 1
    return perimeter


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