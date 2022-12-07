
def read_input(filename):
    with open(filename) as file:
        contents = file.read()
    return contents

def find_buff_start(sig, offset):
    idx = offset
    while True:
        temp_set = set(sig[idx-offset:idx])
        if len(temp_set) == offset:
            return idx
        else:
            idx += 1


def main():
    sig = read_input('input.txt')
    offset = 14
    start_idx = find_buff_start(sig, offset)
    print(start_idx)

if __name__ == "__main__":
    main()