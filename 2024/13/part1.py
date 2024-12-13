def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def parse_lines(lines):
    machines = []
    idx = 0
    for i,line in enumerate(lines):
        counter = i % 4
        if counter == 0:
            _,a = line.split(": ")
            x,y = a.split(", ")
            _,x = x.split("+")
            _,y = y.split("+")
            machines.append({"A":(int(x),int(y))})
            continue
        if counter == 1:
            _,b = line.split(": ")
            x,y = b.split(", ")
            _,x = x.split("+")
            _,y = y.split("+")
            machines[idx]["B"] = (int(x),int(y))
            continue
        if counter == 2:
            _,pz = line.split(": ")
            x,y = pz.split(", ")
            _,x = x.split("=")
            _,y = y.split("=")
            machines[idx]["PZ"] = (int(x),int(y))
            continue
        if counter == 3:
            idx +=1
    return machines


def do_math(machines):
    total = 0
    for claw in machines:
        p2 = 10000000000000
        ax,ay = claw["A"]
        bx,by = claw["B"]
        px,py = claw["PZ"]
        px += p2
        py += p2
        ca = (px*by - py*bx) / (ax*by - ay*bx)
        cb = (px-ax*ca) / bx
        if ca % 1 == cb % 1 == 0:
            total += int(ca * 3 + cb)
    return total


def main():
    lines = read_input("input.txt")
    machines = parse_lines(lines)
    ans = do_math(machines)
    print(ans)
    

if __name__ == "__main__":
    main()