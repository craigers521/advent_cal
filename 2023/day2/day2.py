redmax = 12
greenmax = 13
bluemax = 14

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

def split_lines(lines):
    newlist = []
    for line in lines:
        temp_list = []
        newline = [s.strip() for s in line.split(';')]
        for round in newline:
            round_dict = {}
            cubesplit = round.split(',')
            for cube in cubesplit:
                tempsplit = cube.split()
                round_dict[tempsplit[1]] = tempsplit[0]
            temp_list.append(round_dict)
        newlist.append(temp_list)
    return newlist


def remove_ids(lines):
    r_list = []
    for line in lines:
        newline = line.split(':')
        r_list.append(newline[1].lstrip())
    return r_list


def check_games(glist):
    total = 0
    legal = True
    for id,game in enumerate(glist):
        for round in game:
            if 'red' in round.keys():
                if int(round['red']) > redmax:
                  legal = False
                  break
            if 'green' in round.keys():
                if int(round['green']) > greenmax:
                    legal = False
                    break
            if 'blue' in round.keys():
                if int(round['blue']) > bluemax:
                    legal = False
                    break
        if legal:
            total += id+1
        else:
            legal = True
    return total
            

def find_power(glist):
    total = 0
    for game in glist:
        bblue = 0
        bred = 0
        bgreen = 0
        for round in game:
            if 'red' in round.keys():
                if int(round['red']) > bred:
                    bred = int(round['red'])
            if 'green' in round.keys():
                if int(round['green']) > bgreen:
                    bgreen = int(round['green'])
            if 'blue' in round.keys():
                if int(round['blue']) > bblue:
                    bblue = int(round['blue'])
        total += (bblue*bgreen*bred)
    return total
            

def main():
    lines = read_input("input.txt")
    removed_id_list = remove_ids(lines)
    gameslist = split_lines(removed_id_list)
    valid_total = check_games(gameslist)
    print(valid_total)
    total_power = find_power(gameslist)
    print(total_power)

if __name__ == "__main__":
    main()