def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            lines.append([line[:len(line)//2], line[len(line)//2:]])
    return lines


def find_dupes(sacks):
    dupe_list = []
    for sack in sacks:
        dupe_list.append(list((set(sack[0])&set(sack[1]))))
    return dupe_list


def find_priority(ilist):
    plist = []
    for item in ilist:
        if item[0].isupper():
            plist.append(ord(item[0])-38)
        else:
            plist.append(ord(item[0])-96)
    return plist

def main():
    sacks = read_input('input.txt')
    dupes = find_dupes(sacks)
    priority = find_priority(dupes)
    print(sum(priority))

if __name__ == "__main__":
    main()
