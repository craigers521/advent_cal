def read_input(filename):
    lines = []
    with open(filename) as file:
        lines = file.read().split('\n\n')
        lines = [line.split('\n') for line in lines]
    return lines

def make_grids(lines):
    grids = [[[x for x in y] for y in grid] for grid in lines]
    return grids


def find_mirror(grid, smudge: bool):
    for r in range(1,len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        above = above[:len(below)]
        below = below[:len(above)]
        if not smudge:
            if above == below:
                return r
        else:
            bad = 0
            for y in range(len(above)):
                for x in range(len(above[0])):
                    if above[y][x] != below[y][x]: 
                        bad += 1
            if bad == 1:
                return r
            else:
                continue
    return 0

def find_sym(grids, smudge: bool):
    total = 0
    for grid in grids:
        row = find_mirror(grid, smudge)
        total += row*100
        col = find_mirror(list(zip(*grid)), smudge)
        total += col
    return total




def main():
    lines = read_input("sample.txt")
    grids = make_grids(lines)
    p1 = find_sym(grids, smudge=False)
    print(p1)
    p2 = find_sym(grids, smudge=True)
    print(p2)

    

if __name__ == "__main__":
    main()