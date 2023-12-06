from collections import defaultdict
import math

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def find_wins(lines):
    times,records = [line.split(':')[1].split() for line in lines]
    times = list(map(int,times))
    records = list(map(int,records))
    wins = defaultdict(int)
    for i,record in enumerate(records):
        a = 0
        countdown = times[i]
        for c in range(1,countdown):
            a += 1
            d = a*(countdown-c)
            if d > record:
                wins[i] += 1
    p1 = math.prod(wins.values())
    return p1


def main():
    lines = read_input("input.txt")
    p1 = find_wins(lines)
    print(p1)

if __name__ == "__main__":
    main()