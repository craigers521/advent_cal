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
    safe_total = 0
    for line in lines:
        asc = test_asc(line)
        des = test_des(line)
        if asc or des:
            pass
        else:
            continue
        safe = test_inc(line)
        if safe:
            safe_total += 1
    return safe_total


def test_asc(line):
    asc = True
    idx = 0
    while asc is True:
        if line[idx+1] > line[idx]:
            idx += 1
        else:
            asc = False
        if idx == len(line)-1:
            break
    return asc

def test_des(line):
    des = True
    idx = 0
    while des is True:
        if line[idx+1] < line[idx]:
            idx += 1
        else:
            des = False
        if idx == len(line)-1:
            break
    return des

def test_inc(line):
    safe = True
    for i,x in enumerate(line):
        if abs(x-line[i+1]) > 3:
            safe = False
        if i == len(line)-2:
            break
    return safe




def main():
    lines = read_input("input.txt")
    split_lines = split_input(lines)
    ans = find_safe(split_lines)
    print(ans)
    

if __name__ == "__main__":
    main()