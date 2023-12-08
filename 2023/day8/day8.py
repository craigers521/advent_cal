from math import gcd

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def make_map(lines):
    dirs, *nodelist = lines
    nodelist.pop(0)
    nodes = {}
    for node in nodelist:
        templist = node.split(' = ')
        nodes[templist[0]] = templist[1][1:9].split(', ')
    
    return dirs, nodes


def find_steps(dirs, nodes):
    steps = 0
    char = 0
    node = 'AAA'
    while node != 'ZZZ':
        if dirs[char] == 'L':
            node = nodes[node][0]
        if dirs[char] == 'R':
            node = nodes[node][1]
        char += 1
        if char == len(dirs):
            char = 0
        steps += 1
    return steps


def ghost_steps(dirs, nodes):
    steps = []
    char = 0
    paths = find_keys(nodes, 'A')
    for path in paths:
        temp_steps = 0
        while not path.endswith('Z'):
            if dirs[char] == 'L':
                path = nodes[path][0]
            if dirs[char] == 'R':
                path = nodes[path][1]
            char += 1
            if char == len(dirs):
                char = 0
            temp_steps += 1
        steps.append(temp_steps)
    return find_lcm(steps)

def find_lcm(steps):
    leastcm = 1
    for step in steps:
        leastcm = leastcm*step//gcd(leastcm, step)
    return leastcm

def find_keys(nodes, ch):
    found_keys = []
    for key in nodes.keys():
        if key[2] == ch:
            found_keys.append(key)
    return found_keys

def ending_keys(keys):
    for key in keys:
        if key[2] != 'Z':
            return False
    return True


def main():
    lines = read_input("input.txt")
    dirs, nodes = make_map(lines)
    #p1 = find_steps(dirs,nodes)
    #print(p1)
    p2 = ghost_steps(dirs,nodes)
    print(p2)
    

if __name__ == "__main__":
    main()