def read_input(filename):
    f = open(filename).read().strip()
    return f


def parse_seeds(lines):
    stuff = lines.split('\n\n')
    seeds, *rest = stuff
    seeds = [int(x) for x in seeds.split(':')[1].split()]
    maps = [line.split('\n')[1:] for line in rest]
    return seeds,maps
 
class Mapthing:
    def __init__(self,mappings):
        self.tups = [[int(x) for x in mapping.split()] for mapping in mappings]
    def run_one(self,input):
        for dst,src,rng in self.tups:
            src_end = src+rng
            if src <= input < src_end:
                return dst+(input-src)
        return input
    def run_range(self,interval):
        for dst,src,rng in self.tuples:
            src_end = src+rng
            while interval:
                (start,end) = interval.pop()
                before = (start,min(end,src)) #from seed start to lower of seed range end and source start
                inter = (max(start,src), min(src_end, end)) #higher of seed start and source start to lower of source end and seed end
                after = (max(src_end, start), end) #higher of seed start and source end to seed end
                if before[1] > before[0]:



        
def find_locs(seeds, Mapthings):
    locs = []
    for seed in seeds:
        for Mapthing in Mapthings:
            seed = Mapthing.run_one(seed)
        locs.append(seed)
    return min(locs)

def find_intervals(seedpairs, Mapthings):
    for sseed,eseed in seedpairs:
        seedr = [(sseed, sseed+eseed)]
        for Mapthing in Mapthings:
            seedr = Mapthing.run_range(seedr)
    
def main():
    lines = read_input("input.txt")
    seeds,maps = parse_seeds(lines)
    Mapthings = [Mapthing(map) for map in maps]
    p1 = find_locs(seeds, Mapthings)
    print(p1)
    seedpairs = [seeds[i:i+2] for i in range(0,len(seeds),2)]
    p2 = find_intervals(seedpairs, Mapthings)

if __name__ == "__main__":
    main()