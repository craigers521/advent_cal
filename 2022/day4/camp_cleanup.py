def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def split_pairs(pairs):
    new_list = []
    for pair in pairs:
        new_list.append(pair.split(','))
    return new_list


def split_bounds(alist):
    blist = []
    for pair in alist:
        blist.append([pair[0].split('-'),pair[1].split('-')])
    return blist


def find_contains(bounds):
    count = 0
    for pair in bounds:
        lower1 = int(pair[0][0])
        lower2 = int(pair[1][0])
        upper1 = int(pair[0][1])
        upper2 = int(pair[1][1])
        if lower1 <= lower2 and upper1 >= upper2:
            count += 1
            continue
        if lower2 <= lower1 and upper2 >= upper1:
            count += 1
            continue
    return count


def find_olaps(bounds):
    olaps = 0
    for pair in bounds:
        lower1 = int(pair[0][0])
        lower2 = int(pair[1][0])
        upper1 = int(pair[0][1])
        upper2 = int(pair[1][1])
        r1 = range(lower1, upper1+1)
        r2 = range(lower2, upper2+1)
        set1 = set(r1)
        olap = set1.intersection(r2)
        if olap:
            olaps += 1
    return olaps



def main():
    assns_raw = read_input('input.txt')
    assns = split_pairs(assns_raw)
    bounds_list = split_bounds(assns)
    contains = find_contains(bounds_list)
    print(contains)
    overlaps = find_olaps(bounds_list)
    print(overlaps)


if __name__ == "__main__":
    main()