numdict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

def find_left(line):
    idx2 = []
    numlist = []
    for idx,char in enumerate(line):
        if char.isdigit():
            idx1 = idx
            break
    for num in numdict.keys():
        x = line.find(num)
        if x > -1:
            idx2.append(x)
            numlist.append(numdict[num])
    if len(idx2) > 0:
        minvalidx = idx2.index(min(idx2))
        minvalword = numlist[minvalidx]
    else:
        idx2.append(9999)
    if 'idx1' in locals():
        if idx1 < min(idx2):
          return line[idx1]
        else:
            return minvalword
    else:
        return minvalword


def find_right(line):
    idx2 = []
    numlist = []
    for char in line[::-1]:
        if char.isdigit():
            idx1 = line.rindex(char)
            break
    for num in numdict.keys():
        x = line.rfind(num)
        if x > -1:
            idx2.append(x)
            numlist.append(numdict[num])
    if len(idx2) > 0:
        maxwordidx = idx2.index(max(idx2))
        maxword = numlist[maxwordidx]
    else:
        idx2.append(-1)
    if 'idx1' in locals():
        if idx1 > max(idx2):
          return line[idx1]
        else:
            return maxword
    else:
        return maxword  


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