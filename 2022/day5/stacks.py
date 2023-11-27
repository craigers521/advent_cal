import csv

stacks = {
    "1": ['D','M','S','Z','R','F','W','N'],
    "2": ['W','P','Q','G','S'],
    "3": ['W','R','V','Q','F','N','J','C'],
    "4": ['F','Z','P','C','G','D','L'],
    "5": ['T','P','S'],
    "6": ['H','D','F','W','R','L'],
    "7": ['Z','N','D','C'],
    "8": ['W','N','R','F','V','S','J','Q'],
    "9": ['R','M','S','G','Z','W','V']
}

def read_input(filename):
    ins = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            ins.append(row)
    return ins


def move_stacks(ins):
    for moves in ins:
        counter = int(moves[0])
        while counter > 0:
            stacks[moves[2]].append(stacks[moves[1]].pop())
            counter -= 1


def move_multi(ins):
    for moves in ins:
        crates = int(moves[0])
        start = moves[1]
        finish = moves[2]
        #items_to_move = stacks[start][-crates:]
        stacks[finish].extend(stacks[start][-crates:])
        stacks[start] = stacks[start][:-crates]

def read_tops():
    temp_list = []
    temp_str = ""
    for stack in stacks.values():
        temp_list.append(stack[-1])
    for val in temp_list:
        temp_str += val
    return temp_str

def main():
    ins = read_input('input_scrubbed.csv')
    #move_stacks(ins)
    move_multi(ins)
    tops = read_tops()
    print(tops)

if __name__ == "__main__":
    main()