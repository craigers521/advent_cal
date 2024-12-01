def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def split_sort(lines):
    left = []
    right = []
    for line in lines:
        l,r = line.split()
        left.append(int(l))
        right.append(int(r))
    left = sorted(left)
    right = sorted(right)
    return left, right

def find_diffs(left, right):
    diffs = []
    for idx, val in enumerate(left):
        diffs.append(abs(val-right[idx]))
    return diffs





def main():
    lines = read_input("input.txt")
    left,right = split_sort(lines)
    diffs = find_diffs(left, right)
    ans = sum(diffs)
    print(ans)
    

if __name__ == "__main__":
    main()