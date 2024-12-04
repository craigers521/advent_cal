P = complex
adj = [P(-1,-1), P(0,-1), P(1,-1),
       P(-1,0),           P(1,0),
       P(-1,1),  P(0,1),  P(1,1)]

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

def find_matches(grid):
    total = 0
    for coord in grid:
        for d in adj:
            pos = coord
            if grid[coord] == 'X':
                pos += d
                if pos in grid and grid[pos] == 'M':
                    pos += d
                    if pos in grid and grid[pos] == 'A':
                        pos += d
                        if pos in grid and grid[pos] == 'S':
                            total += 1
    return total

def main():
    lines = read_input("input.txt")
    grid = make_grid(lines)
    ans = find_matches(grid)
    print(ans)

if __name__ == "__main__":
    main()