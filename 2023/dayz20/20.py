from collections import deque

class Module:

    def __init__(self, mod, name, dst):
        self.mod = mod
        self.name = name
        self.dst = dst
        self.state = 'off'
        self.mem = {}

    def prop(self, input, src):
        if self.mod == '%' and input == 'lo':
            if self.state == 'off': 
                self.state = 'on'
                return (self.dst, 'hi', self.name)
            else: 
                self.state = 'off'
                return (self.dst, 'lo', self.name)
        elif self.mod == '%' and input == 'hi':
            return ([None],None,None)
        elif self.mod == '&':
            self.mem[src] = input
            if all(x == 'hi' for x in self.mem.values()):
                return (self.dst, 'lo', self.name)
            else:
                return (self.dst, 'hi', self.name)
        elif self.mod == 'broadcast':
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
                modules[d].mem[name] = 'lo'
    return modules


def propagate(modules, count):
    modules = init_state(modules)
    input = 'lo'
    src = 'button'
    dst = 'broadcaster'
    hilo = [0,0]
    seen = {}
    for i in range(count):
        Q = deque([(dst, input, src)])
        hilo = pulse(Q, modules, hilo, i, seen)
    print(seen) # im gonna bullshit this and use an online LCM calculator i'm done
    return hilo

def pulse(Q, modules, hilo, cycle, seen):
    while Q:
        dst,input,src = Q.popleft()
        if dst == 'kh' and input == 'hi':
            seen[src] = cycle+1
        #print(f"{src} -{input} -> {dst}")
        if input == 'hi': hilo[0] += 1
        elif input == 'lo': hilo[1] += 1
        if dst is not None and dst in modules:
            out,inc,org = modules[dst].prop(input,src)
        else:
            continue
        for o in out:
            Q.append([o,inc,org])
    return hilo


def main():
    lines = read_input("input.txt")
    modules = make_mods(lines)
    hilo = propagate(modules, 5000)
    print(hilo[0]*hilo[1])
    

if __name__ == "__main__":
    main()