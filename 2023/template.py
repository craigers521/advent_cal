def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def main():
    lines = read_input("sample.txt")
    

if __name__ == "__main__":
    main()