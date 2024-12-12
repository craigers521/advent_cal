def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def read_disk(input):
    disk = {}
    blanks = []
    id = 0
    pos = 0
    for i, char in enumerate(input):
        x = int(char)
        if i % 2 == 0:
            disk[id] = (pos, x)
            id += 1
        else:
            if x != 0:
                blanks.append((pos, x))
        pos += x
    return disk, blanks, id


def disk_compress(disk, blanks, id):
    while id > 0:
        id -= 1
        pos, size = disk[id]
        for i, (start, length) in enumerate(blanks):
            if start >= pos:
                blanks = blanks[:i]
                break
            if size <= length:
                disk[id] = (start, size)
                if size == length:
                    blanks.pop(i)
                else:
                    blanks[i] = (start+size, length-size)
                break
    checksum = find_checksum(disk)
    return checksum


def find_checksum(disk):
    total = 0
    for id, (pos, size) in disk.items():
        for x in range(pos, pos+size):
            total += id*x
    return total


def main():
    lines = read_input("input.txt")
    disk, blanks, id = read_disk(lines[0])
    ans = disk_compress(disk, blanks, id)
    print(ans)
    

if __name__ == "__main__":
    main()