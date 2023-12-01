

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

def find_left(line):
    for char in line:
        if char.isdigit():
            return char
        else: 
            pass


def find_right(line):
    line = line[::-1]
    for char in line:
        if char.isdigit():
            return char
        else:
            pass


def build_list(lines):
    values = []
    for line in lines:
        left = find_left(line)
        right = find_right(line)
        values.append(left+right)
    return values

def sumvals(values):
    return sum([int(i) for i in values])


def main():
    lines = read_input("input.txt")
    values = build_list(lines)
    calibration = sumvals(values)
    print(calibration)
    


if __name__ == "__main__":
    main()