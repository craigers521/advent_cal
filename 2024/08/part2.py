from collections import defaultdict

P = complex

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def make_grid(lines):
    grid = {}
    ants = defaultdict(list)
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            grid[P(x,y)] = val
            if val != ".":
                ants[val].append(P(x,y))
    return grid, ants


def find_nodes(grid, ants):
    nodes = set()
    for ant in ants:
        pairs = get_pairs(ants[ant])
        for pair in pairs:
            d = pair[1] - pair[0]
            node1 = pair[1] + d
            node2 = pair[0] - d
            node3 = pair[0] + d
            node4 = pair[1] - d
            while node1 in grid:
                grid[node1] = "#"
                nodes.add(node1)
                node1 += d
            while node2 in grid:
                grid[node2] = "#"
                nodes.add(node2)
                node2 -= d
            while node3 in grid:
                grid[node3] = "#"
                nodes.add(node3)
                node3 += d
            while node4 in grid:
                grid[node4] = "#"
                nodes.add(node4)
                node4 -= d
    return nodes


def get_pairs(mylist):
    pair_list = []
    for i in range(len(mylist)):
        for j in range(i+1, len(mylist)):
            pair_list.append((mylist[i], mylist[j]))
    return pair_list


def print_grid(grid):
    for pos in grid:
        if pos.real == 0:
            print("\n")
        print(grid[pos], end='')
    return

def main():
    lines = read_input("input.txt")
    grid, ants = make_grid(lines)
    nodes = find_nodes(grid, ants)
    #print_grid(grid)
    print(len(nodes))
    

if __name__ == "__main__":
    main()