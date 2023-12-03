P = complex
adj = [P(-1,-1), P(0,-1), P(1,-1),
       P(-1,0),           P(1,0),
       P(-1,1),  P(0,1),  P(1,1)]

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
            if val != '.':
              grid[P(x,y)] = val
    return grid

def get_symbols(grid):
    symbols = []
    for k,v in grid.items():
        if not v.isnumeric():
            symbols.append(k)
    return symbols


def find_num(grid, pos):
    if pos not in grid or not grid[pos].isnumeric():
        return
    while pos-1 in grid and grid[pos-1].isnumeric():
        pos -= 1
    start = pos
    num = ''
    while pos in grid and grid[pos].isnumeric():
        num += grid[pos]
        pos += 1
    return start, int(num)


def find_adj(grid, pos):
    parts = set()
    for d in adj:
        parts.add(find_num(grid, pos+d))
    parts.remove(None)
    return parts


def find_parts(grid, symbols):
    parts = set()
    for s in symbols:
        parts.update(find_adj(grid, s))
    p1 = 0
    for part in parts:
        p1 += part[1]
    return p1


def find_gears(grid, symbols):
    total = 0
    for s in symbols:
        if grid[s] != '*': continue
        parts = list(find_adj(grid, s))
        if len(parts) == 2:
            total += parts[0][1]*parts[1][1]
    return total

def main():
    lines = read_input("input.txt")
    grid = make_grid(lines)
    symbols = get_symbols(grid)
    p1 = find_parts(grid, symbols)
    p2 = find_gears(grid, symbols)
    print(p1, p2)


if __name__ == "__main__":
    main()