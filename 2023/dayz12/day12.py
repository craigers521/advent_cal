import itertools

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def parse_input(lines):
    records = [[x.split(',') for x in line.split()] for line in lines]
    for record in records:
        record[1] = list(map(int,record[1]))
    return records

def find_perms(records):
    p1 = 0
    for record in records:
        springs,conds = record[0][0],record[1]
        p1+= make_perms(springs,conds)
    return p1

def make_perms(springs, conds):
    ans = 0
    perm_list = []
    spring_list = []
    springrps = springs.split('.')
    for grp in springrps:
        if '?' in grp:
            perms = list(itertools.product(('#','.'), repeat=grp.count('?')))
            temp_list = []
            for perm in perms:
                temp_list.append(''.join(perm))
            perm_list.append(temp_list)
        else:
            perm_list.append(grp)
    ######## insert working function to concatenate all possible string permuations here
    # then do some for loop to eval all functions 
    for somebullshit in listofbullshit:
        grplngs = list(map(len, springrps))
        if grplngs == conds:
            ans += 1
    return ans


def main():
    lines = read_input("sample.txt")
    records = parse_input(lines)
    p1 = find_perms(records)
    

if __name__ == "__main__":
    main()