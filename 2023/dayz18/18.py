def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def find_bounds(lines):
    dirs = {'R': (1,0), 'L': (-1,0), 'U': (0,-1), 'D': (0,1)}
    points = [(0,0)]
    perimeter = 0
    for line in lines:
        d, n, _ = line.split()
        dr, dc = dirs[d]
        n = int(n)
        perimeter += n
        r,c = points[-1]
        points.append((r+dr*n, c+dc*n ))
    return points, perimeter

def find_bounds2(lines):
    dirs = {'R': (1,0), 'L': (-1,0), 'U': (0,-1), 'D': (0,1)}
    points = [(0,0)]
    perimeter = 0
    for line in lines:
        d, n = line[0],line[1]
        dr, dc = dirs[d]
        perimeter += n
        r,c = points[-1]
        points.append((r+dr*n, c+dc*n ))
    return points, perimeter


def find_area(points, perimeter):
    a1,a2 = 0,0
    xs = []
    ys = []
    for point in points:
        xs.append(point[0])
        ys.append(point[1])
    for i in range(len(xs)-1):
        a1 += xs[i]*ys[i+1]
        a2 += ys[i]*xs[i+1]
    intarea = abs(a1-a2)//2   # shoelace formula
    area = intarea - (perimeter//2) + 1 # picks theorum
    return area

def parse_hex(lines):
    instr = []
    dirs = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
    for line in lines:
        hex = line.split()[2]
        d = hex[-2]
        n = hex[2:-2]
        n = int(n, 16)
        instr.append((dirs[d], n))
    return instr


def main():
    lines = read_input("input.txt")
    points,perimeter = find_bounds(lines)
    area = find_area(points, perimeter)
    print(area+perimeter)
    instructs = parse_hex(lines)
    points,perimeter = find_bounds2(instructs)
    area = find_area(points, perimeter)
    print(area+perimeter)


if __name__ == "__main__":
    main()