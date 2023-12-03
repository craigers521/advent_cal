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
    print(symbols)


def main():
    lines = read_input("test_grid.txt")
    grid = make_grid(lines)
    symbols = get_symbols(grid)
    for key in grid.keys():
        print(f"{key.real}, {key.imag} = {grid[key]}")
    for _ in adj:
        if P(1,1)+_ in grid: print(grid[P(1,1)+_])
    

if __name__ == "__main__":
    main()