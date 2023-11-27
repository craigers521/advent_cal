check_cycle = [0, 220, 180, 140, 100, 60, 20]

def read_input(filename):
    with open(filename) as file:
        lines =[line.rstrip() for line in file ]
    return lines


def insert_cycle(input):
    output = []
    for inst in input:
        if inst[:4] == 'addx':
            output.append('noop')
        output.append(inst)
    return output


def find_sig(prog):
    sig_str = []
    cycle = 1
    x = 1
    for instr in prog:
        if cycle == check_cycle[-1]:
            sig_str.append(x*check_cycle[-1])
            check_cycle.pop()
        if instr[:4] == 'addx':
            x += int(instr[4:])
        cycle += 1
    return sig_str

def make_crt():
    pixels = []
    for _ in range(6):
        row = ["." for _ in range(40)]
        pixels.append(row)
    return pixels

def find_pixels(prog, pixels):
    cycle = 1
    x = 1
    row = 0
    pos = 0
    for instr in prog:
        if pos == x or pos == x-1 or pos == x+1:
            pixels[row][pos] = "#"
        if cycle % 40 == 0:
            row += 1
            pos -= 40
        if instr[:4] == 'addx':
            x += int(instr[4:])
        cycle += 1
        pos += 1
    return pixels


def print_screen(crt):
    for line in crt:
        print(*line, end = '')
        print()



def main():
    raw_instr = read_input('input.txt')
    pad_instr = insert_cycle(raw_instr)
    #sig_str = find_sig(pad_instr)
    #print(sum(sig_str))
    screen = make_crt()
    #print_screen(screen)
    disp_out = find_pixels(pad_instr, screen)
    print_screen(disp_out)

if __name__ == "__main__":
    main()