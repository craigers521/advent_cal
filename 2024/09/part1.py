def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def read_disk(input):
    disk = []
    id = 0
    for i, char in enumerate(input):
        x = int(char)
        if i % 2 == 0:
            disk += [id]*x
            id += 1
        else:
            disk += [-1]*x
    return disk


def disk_compress(disk):
    blanks = find_blanks(disk)
    for i in blanks:
        while disk[-1] == -1: disk.pop()
        if len(disk) <= i: break
        file = disk.pop()
        disk[i] = file
    checksum = find_checksum(disk)
    return checksum


def find_checksum(disk):
    total = 0
    for i,x in enumerate(disk):
        total += i*int(x)
    return total

def find_blanks(disk):
    blanks = []
    for i,val in enumerate(disk):
        if val == -1: blanks.append(i)
    return blanks


def main():
    lines = read_input("input.txt")
    disk_map = read_disk(lines[0])
    ans = disk_compress(disk_map)
    print(ans)
    

if __name__ == "__main__":
    main()