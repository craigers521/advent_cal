from collections import deque

P = complex

U = P(0, -1)
R = P(1,0)
D = P(0,1)
L = P(-1,0)

dirs = [U,R,D,L]

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def make_grid(lines):
    grid = {}
    trailheads = []
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
            grid[P(x,y)] = int(val)
            if val == "0": 
                trailheads.append(P(x,y))
    return grid, trailheads


def find_trails(grid, heads):
    score = 0
    for start in heads:
        q = deque([start])
        seen = {start}
        summits = 0
        while len(q) > 0:
            pos = q.popleft()
            for dir in dirs:
                step = pos+dir
                if step not in grid: continue
                if grid[step] != grid[pos] + 1: continue
                #if step in seen: continue
                seen.add(step)
                if grid[step] == 9:
                    summits +=1
                else: q.append(step)
        score += summits
    return score



def main():
    lines = read_input("input.txt")
    grid, heads = make_grid(lines)
    ans = find_trails(grid, heads)
    print(ans)

if __name__ == "__main__":
    main()