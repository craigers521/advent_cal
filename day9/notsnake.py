

def read_input(filename):
    with open(filename) as file:
        lines = file.read().split('\n')
    return lines


def main():
    moves = read_input('sample.txt')
    print(moves)

if __name__ == "__main__":
    main()