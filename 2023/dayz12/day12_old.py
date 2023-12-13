import functools

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



def main():
    lines = read_input("sample.txt")
    records = parse_input(lines)
    p1 = find_perms(records)
    

if __name__ == "__main__":
    main()