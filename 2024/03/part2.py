
def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def parse_lines(lines):
    total = 0
    do = True
    for line in lines:
        for i in range(len(line)-3):
            substring = line[i:i+4]
            if "do" in substring:
                if substring == "do()":
                    do = True
                elif substring == "don'":
                    do = False
            if do:
                if substring == "mul(":
                    j = i+5
                    while line[j] != ")":
                        if j+1 > len(line):
                            break
                        j +=1
                    multiples = line[i+4:j]
                    if multiples.count(",") == 1:
                        x,y = multiples.split(",")
                        if x.isdigit() and y.isdigit():
                            total += int(x)*int(y)
    return total

def main():
    lines = read_input("input.txt")
    ans = parse_lines(lines)
    print(ans)
    

if __name__ == "__main__":
    main()