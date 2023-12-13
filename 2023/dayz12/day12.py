#from functools import lru_cache
from datetime import datetime

cache = {}

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def parse_input(lines):
    records = [[x.split(',') for x in line.split()] for line in lines]
    return records


#@lru_cache
def get_counts(springs, blocks):
    if blocks == ():
        if '#' not in springs:
            return 1
        else:
            return 0
    if springs == "":
        if blocks == ():
            return 1
        else:
            return 0

    key = (springs, blocks)
    if key in cache:
        return cache[key]
    
    result = 0
    if springs[0] in '.?':
        result += get_counts(springs[1:], blocks)
    if springs[0] in '#?':
        if valid_block(springs, blocks[0]):
            result += get_counts(springs[1+blocks[0]:], blocks[1:])
    
    cache[key] = result
    return result

def valid_block(springs,block):
    if len(springs) < block:
        return False
    if '.' in springs[:block]:
        return False
    if len(springs) > block and springs[block] == '#':
        return False
    return True


def main():
    lines = read_input("input.txt")
    records = parse_input(lines)
    p1 = 0
    for record in records:
        p1 += get_counts(record[0][0], tuple(map(int, record[1])))
    print(p1)
    p2 = 0
    start = datetime.now()
    for record in records:
        springs = '?'.join(record[0]*5)
        blocks = tuple(map(int, record[1]))*5
        p2 += get_counts(springs, blocks)
    print(p2)
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    print(f"execution time: {td}ms")

    

if __name__ == "__main__":
    main()