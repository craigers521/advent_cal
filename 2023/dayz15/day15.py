from collections import defaultdict
cache = {}
cache2 = {}

def read_input(filename):
    with open(filename) as file:
        lines = file.read().split(',')
    return lines

def run_hash(seq):
    total = 0
    for step in seq:
        if step in cache:
            total += cache[step]
        else:
            result = hash(step)
            cache[step] = result
            total += result
    return total

def hash(step):
    val = 0
    if step in cache2:
        counter += 1
        return cache2[step]
    for c in step:
        val += ord(c)
        val = val*17
        val = val%256
    cache2[step] = val
    return val
        

def slot_lenses(seq,boxes):
    for step in seq:
        if '=' in step:
            label,focus = step.split('=')
            box = hash(label)
            for i,lens in enumerate(boxes[box]):
                if label in boxes[box][i]:
                    boxes[box][i][label] = focus
                    break
            else:
                boxes[box].append({label:focus})
        if step[-1] == '-':
            label = step[:-1]
            box = hash(label)
            for lens in boxes[box]:
                if label in lens:
                    boxes[box].pop(boxes[box].index(lens))
    return boxes
        

def find_power(boxes):
    power = 0
    for num,box in enumerate(boxes):
        for slot,lens in enumerate(box):
            power += ((num+1)*(slot+1)*(int(list(lens.values())[0])))
    return power


def main():
    seq = read_input("input.txt")
    #p1 = run_hash(seq)
    #print(p1)
    boxes = []
    for _ in range(256):
        boxes.append([])
    fullboxes = slot_lenses(seq,boxes)
    p2 = find_power(fullboxes)
    print(p2, counter)

    

if __name__ == "__main__":
    main()