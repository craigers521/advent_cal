from collections import deque

P = complex

U = P(0, -1)
R = P(1,0)
D = P(0,1)
L = P(-1,0)

dirs = [U,R,D,L]

f = open("output.txt", "w")

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def parse_lines(lines):
    robots = []
    for line in lines:
        p,v = line.split()
        _,p = p.split("=")
        px,py = p.split(",")
        _,v = v.split("=")
        vx,vy = v.split(",")
        px,py,vx,vy = map(int, (x for x in [px,py,vx,vy]))
        robots.append({"px":px,"py":py,"v":(vx,vy)})
    return robots


def build_grid(x, y, robots):
    grid ={}
    for i in range(y):
        for j in range(x):
            grid[P(j,i)] = 0
    for bot in robots:
        sx = bot["px"]
        sy = bot["py"]
        grid[P(sx,sy)] += 1
    return grid


def move_robots(robots, grid, sec, max_x, max_y):
    while sec:
        for bot in robots:
            vx, vy = bot["v"]
            px,py = bot["px"], bot["py"]
            grid[P(px,py)] -= 1
            if px + vx < 0:
                newx = max_x + (px+vx)
            elif px + vx > max_x-1:
                newx = (px+vx)-max_x
            else:
                newx = px+vx
            if py + vy < 0:
                newy = max_y + (py+vy)
            elif py + vy > max_y-1:
                newy = (py+vy)-max_y
            else:
                newy = py+vy
            bot["px"] = newx
            bot["py"] = newy
            grid[P(newx,newy)] += 1
        sec -= 1
        connected = find_conn(grid)
        if max(connected) > 200:
            print_grid(grid, sec)
    return grid

def find_conn(grid):
    master_seen = set()
    comp = []
    for point in grid:
        if grid[point] == 0: continue
        if point in master_seen: continue
        seen = {point}
        q = deque([point])
        count = 0
        while q:
            pos = q.popleft()
            for dir in dirs:
                step = pos+dir
                if step not in grid: continue
                if grid[step] == 0: continue
                if step in seen: continue
                seen.add(step)
                q.append(step)
                count += 1
        master_seen.update(seen)
        comp.append(count)
    return comp


def print_grid(grid, sec):
    print(f"Step: {10000-sec}", file=f)
    for pos in grid:
        if pos.real == 0:
            print("", file=f)
        if grid[pos] == 0: print(".", end='', file=f)
        else: print("#", end='', file=f)
    print("\n", file=f)
    print("-"*100, file=f)
    print("\n", file=f)
    return

def find_quads(grid,x,y):
    skipx = x//2
    skipy = y//2
    q1 = q2 = q3 = q4 = 0
    for pos in grid:
        if pos.real < skipx and pos.imag < skipy:
            q1 += grid[pos]
        elif pos.real > skipx and pos.imag < skipy:
            q2 += grid[pos]
        elif pos.real < skipx and pos.imag > skipy:
            q3 += grid[pos]
        elif pos.real > skipx and pos.imag > skipy:
            q4 += grid[pos]
        else:
            continue
    return q1*q2*q3*q4



def main():
    lines = read_input("input.txt")
    robots = parse_lines(lines)
    x,y = 101,103
    sec = 10000
    grid = build_grid(x, y, robots)
    grid = move_robots(robots, grid, sec, x, y)
    ans = find_quads(grid,x,y)
    print(ans)
    
    

if __name__ == "__main__":
    main()