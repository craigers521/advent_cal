from tqdm import tqdm

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def parse_stones(input):
    stones = input[0].split()
    return stones


def blink(stones, counter):
    for _ in tqdm(range(counter)):
        output = []
        for rock in stones:
            if rock == "0":
                output.append("1")
                continue
            if len(rock) % 2 == 0:
                left = rock[:len(rock)//2]
                right = rock[len(rock)//2:]
                right = str(int(right))
                output.append(left)
                output.append(right)
            else:
                output.append(str(int(rock)*2024))
        stones = output
    return len(stones)

def main():
    lines = read_input("input.txt")
    stones = parse_stones(lines)
    ans = blink(stones, 25)
    print(ans)
    

if __name__ == "__main__":
    main()