P = complex

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def map_space(lines):
    rows = len(lines)
    cols = len(lines[0])
    empty = [set(range(cols)), set(range(rows))]
    galaxies = []
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
              if val == '#':
                  galaxies.append(P(x,y))
                  empty[0] -= {x}   # assume space is empty, remove from set if not
                  empty[1] -= {y}   # use set subtraction to not deal with val not in list
    return galaxies, empty


def expand_space(space,empty):
    xspace = []
    for galaxy in space:
        shift = P(
            sum(x<galaxy.real for x in empty[0]), #sum boolean Trues as 1s to get shift amount
            sum(y<galaxy.imag for y in empty[1])
        )*(100-1) #multiply by factor of expansion 
        xspace.append(galaxy+shift)
    return xspace


def find_dist(space):
    p1 = 0
    pairs = [(a,b) for idx,a in enumerate(space) for b in space[idx+1:]]
    for pair in pairs:
        p1 += calc_dist(pair[0], pair[1])
    return p1


def calc_dist(a, b):
    diff = a-b
    return int(abs(diff.real)+abs(diff.imag))


def main():
    lines = read_input("sample.txt")
    galaxies,empty = map_space(lines)
    xspace = expand_space(galaxies,empty)
    p1 = find_dist(xspace)
    print(p1)

if __name__ == "__main__":
    main()