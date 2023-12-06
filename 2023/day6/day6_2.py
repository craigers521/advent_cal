from collections import defaultdict
import math
from datetime import datetime


def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def find_wins(lines):
    times,records = [line.split(':')[1].split() for line in lines]
    ttime = eval(''.join(times))
    trecord = eval(''.join(records))
    wins = 0
    a = 0
    for c in range(1,ttime):
        a += 1
        d = a*(ttime-c)
        if d > trecord:
            wins += 1
    return wins


def quad(lines):
    times,records = [line.split(':')[1].split() for line in lines]
    time = eval(''.join(times))
    record = eval(''.join(records))
    delta =  (time**2 - 4*record)**0.5
    lo,hi = (time-delta)/2, (time+delta)/2
    return math.ceil(hi) - math.floor(lo) -1


def main():
    lines = read_input("input.txt")
    s1 = datetime.now()
    slow = find_wins(lines)
    e1 = datetime.now()
    print(f"Slow Answer: {slow} took {(e1-s1).total_seconds()*10**3}ms")
    s2 = datetime.now()
    fast = quad(lines)
    e2 = datetime.now()
    print(f"Fast Answer: {fast} took {(e2-s2).total_seconds()*10**3}ms")

if __name__ == "__main__":
    main()