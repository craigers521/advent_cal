def read_input(filename):
    groups = []
    temp_list = []
    counter = 0
    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            temp_list.append(line)
            counter += 1
            if counter == 3:
                counter = 0
                groups.append(temp_list.copy())
                temp_list.clear()            
    return groups


def find_badges(groups):
    badges = []
    for group in groups:
        badges.append(list((set(group[0])&set(group[1])&set(group[2]))))
    return badges


def find_priority(ilist):
    plist = []
    for item in ilist:
        if item[0].isupper():
            plist.append(ord(item[0])-38)
        else:
            plist.append(ord(item[0])-96)
    return plist

def main():
    groups = read_input('input.txt')
    badges = find_badges(groups)
    priority = find_priority(badges)
    print(sum(priority))

if __name__ == "__main__":
    main()