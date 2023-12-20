from collections import defaultdict, deque

class Module:

    def __init__(self, mod, name, dst):
        self.mod = mod
        self.name = name
        self.dst = dst
        self.state = 0
        self.mem = defaultdict(int)

    def prop(self, input, src):
        if self.mod == '%' and input == 0:
            if self.state == 0: 
                self.state = 1
                return (self.dst, 1, self.name)
            else: 
                self.state = 0
                return (self.dst, 0, self.name)
        elif self.mod == '%' and input == 1:
            return (None,None,None)
        elif self.mod == '&':
            self.mem[src] = input
            if all(self.mem.values()):
                return (self.dst, 0, self.name)
            else:
                return (self.dst, 1, self.name)
        else:
            return (self.dst, input, self.name)


def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def make_mods(lines):
    mod_dict = {}
    for line in lines:
        fh,sh = line.split(' -> ')
        if fh[0] == 'b':
            mod,name = 'broadcast', 'broadcaster'
        else:
            mod,name = fh[0],fh[1:]
        if ',' in sh:
            dst = [dst.strip() for dst in sh.split(',')]
        else:
            dst = [sh]
        mod_dict[name] = Module(mod, name, dst)
    return mod_dict
        
def init_state(modules):
    for name, module in modules.items():
        for d in module.dst:
            if d in modules and modules[d].mod == '&':
                modules[d].mem[name] = 0
    return modules


def propagate(modules, count):
    modules = init_state(modules)
    input = 0
    src = 'button'
    dst = 'broadcaster'
    hilo = [0,0]
    for _ in range(count):
        Q = deque([(dst, input, src)])
        hilo = pulse(Q, modules, hilo)
    return hilo

def pulse(Q, modules, hilo):
    while Q:
        dst,input,src = Q.popleft()
        if input == 1: hilo[0] += 1
        else: hilo[1] += 1
        dst,input,src = modules[dst].prop(input,src)
        if dst == None or dst[0] not in modules:
            continue
        for d in dst:
            Q.append([d,input,src])
    return hilo


def main():
    lines = read_input("sample2.txt")
    modules = make_mods(lines)
    hi,lo = propagate(modules, 1000)
    print(hi*lo)
    

if __name__ == "__main__":
    main()