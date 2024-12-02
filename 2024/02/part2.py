def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def split_input(lines):
    split_lines = []
    for line in lines:
        split = [int(x) for x in line.split()]
        split_lines.append(split)
    return split_lines


def find_safe(lines):
    safe = 0
    for line in lines:
        good = False
        for j in range(len(line)):
            damp = line[:j]+line[j+1:]
            if is_safe(damp):
                good = True
        if good:
            safe += 1
    return safe


def is_safe(line):
    is_sorted = (line==sorted(line) or line==sorted(line, reverse=True))
    good = True
    for i in range(len(line)-1):
        diff = abs(line[i]-line[i+1])
        if not 1<=diff<=3:
            good = False
    return is_sorted and good


def main():
    lines = read_input("input.txt")
    split_lines = split_input(lines)
    ans = find_safe(split_lines)
    print(ans)
    

if __name__ == "__main__":
    main()