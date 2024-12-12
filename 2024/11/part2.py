from functools import cache

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def parse_stones(input):
    stones = input[0].split()
    return stones

@cache
def blink(stone, counter):
    if counter == 0: 
        return 1
    if stone == "0":
        return blink("1", counter-1)
    if len(stone) % 2 == 0:
        left = stone[:len(stone)//2]
        right = stone[len(stone)//2:]
        right = str(int(right))
        return blink(left, counter-1) + blink(right, counter-1)
    return blink(str(int(stone)*2024), counter-1)


def main():
    lines = read_input("input.txt")
    stones = parse_stones(lines)
    ans = sum(blink(stone, 75) for stone in stones)
    print(ans)
    

if __name__ == "__main__":
    main()