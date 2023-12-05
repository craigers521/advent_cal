def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def build_maps(lines):
    seeds = lines[0].split(': ')[1]
    rest = [lines[i] for i in range(2,len(lines))]
    rest,s2s = poplines(rest)
    rest,s2f = poplines(rest)
    rest,f2w = poplines(rest)
    rest,w2l = poplines(rest)
    rest,l2t = poplines(rest)
    rest,t2h = poplines(rest)
    h2l = poplines(rest)
    seeds = [int(seed) for seed in seeds.split()]
    seedic = {}
    for seed in seeds:
        seedic[seed] = []
    maps = {'s2s': s2s, 's2f': s2f, 'f2w': f2w, 'w2l': w2l, 'l2t': l2t, 't2h': t2h, 'h2l': h2l}
    return seedic, maps


def poplines(lines):
    templist = []
    while len(lines) > 0:
        tempval = lines.pop(0)
        if ':' in tempval:
            continue
        elif tempval == '':
            return lines,templist
        else:
            templist.append([int(x) for x in tempval.split()])
    return templist


def journey(seeds, maps):
    locs = []
    for seed in seeds:
        soil = findmapping(seed,maps['s2s'])
        seeds[seed].append(soil)
        fert = findmapping(soil,maps['s2f'])
        seeds[seed].append(fert)
        water = findmapping(fert,maps['f2w'])
        seeds[seed].append(water)
        light = findmapping(water,maps['w2l'])
        seeds[seed].append(light)
        temp = findmapping(light,maps['l2t'])
        seeds[seed].append(temp)
        humid = findmapping(temp,maps['t2h'])
        seeds[seed].append(humid)
        loc = findmapping(humid,maps['h2l'])
        seeds[seed].append(loc)
        locs.append(loc)
    return min(locs)


def findmapping(seed, maplist):
    for maps in maplist:
        start = maps[1]
        end = maps[1]+maps[2]-1
        if start <= seed <= end:
            return maps[0]+(seed-start)
    return seed
        
    
def main():
    lines = read_input("input.txt")
    seeds,maps = build_maps(lines)
    p1 = journey(seeds, maps)
    print(p1)

if __name__ == "__main__":
    main()