
def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def make_history(lines):
    history = [[int(x) for x in line.split()] for line in lines]
    return history


def find_deltas(line):
    delta = []
    for i in range(1,len(line)):
        delta.append(line[i]-line[i-1])
    return delta


def predict(history):
    predictions = []
    for line in history:
        deltas = [find_deltas(line)]
        i = 0
        while len(set(deltas[i])) > 1:
            deltas.append(find_deltas(deltas[i]))
            i += 1
        step = deltas[i][-1]
        while i > 0:
            i -= 1
            deltas[i].append(deltas[i][-1]+step)
            step = deltas[i][-1]
        line.append(line[-1]+step)
        predictions.append(line[-1])
    return sum(predictions)


def backwards(history):
    predictions = []
    for line in history:
        deltas = [find_deltas(line)]
        i = 0
        while len(set(deltas[i])) > 1:
            deltas.append(find_deltas(deltas[i]))
            i += 1
        step = deltas[i][0]
        while i > 0:
            i -= 1
            deltas[i].insert(0,deltas[i][0]-step)
            step = deltas[i][0]
        line.insert(0,line[0]-step)
        predictions.append(line[0])
    return sum(predictions)


def main():
    lines = read_input("input.txt")
    history = make_history(lines)
    p1 = predict(history)
    print(p1)
    p2 = backwards(history)
    print(p2)
    

if __name__ == "__main__":
    main()