P = complex

class Beam:
    
    DOWN = P(0,1)
    RIGHT = P(1,0)
    UP = P(0,-1)
    LEFT = P(-1,0)

    def __init__(self, pos, bdir):
        self.pos = pos
        self.bdir = bdir
        self.active = True

    def move_empty(self):
        self.pos += self.bdir

    def move_trav(self, trav):
        if trav == self.bdir:
            self.active = False
        elif trav in (self.LEFT, self.RIGHT) and self.bdir in (self.LEFT, self.RIGHT):
            self.active = False
        elif trav in (self.UP, self.DOWN) and self.bdir in (self.UP, self.DOWN):
            self.active = False
        else:
            self.pos += self.bdir
    
    def move_splitter(self, splitter, cpos):
        if splitter == '-':
            if self.bdir in (self.UP, self.DOWN):
                self.pos += self.RIGHT
                self.bdir = self.RIGHT
                return cpos+self.LEFT, self.LEFT
            else:
                self.pos += self.bdir
                return 0,0
        if splitter == "|":
            if self.bdir in (self.LEFT, self.RIGHT):
                self.pos += self.UP
                self.bdir = self.UP
                return cpos+self.DOWN, self.DOWN
            else:
                self.pos += self.bdir
                return 0,0

    def move_mirror(self, mirror):
        if mirror == "/":
            if self.bdir == self.DOWN:
                self.bdir = self.LEFT
                self.pos += self.LEFT
            elif self.bdir == self.RIGHT:
                self.bdir = self.UP
                self.pos += self.UP
            elif self.bdir == self.UP:
                self.bdir = self.RIGHT
                self.pos += self.RIGHT
            elif self.bdir == self.LEFT:
                self.bdir = self.DOWN
                self.pos += self.DOWN
        if mirror == "\\":
            if self.bdir == self.DOWN:
                self.bdir = self.RIGHT
                self.pos += self.RIGHT
            elif self.bdir == self.RIGHT:
                self.bdir = self.DOWN
                self.pos += self.DOWN
            elif self.bdir == self.UP:
                self.bdir = self.LEFT
                self.pos += self.LEFT
            elif self.bdir == self.LEFT:
                self.bdir = self.UP
                self.pos += self.UP

    def get_pos(self):
        return self.pos
    
    def get_dir(self):
        return self.bdir
    
    def get_active(self):
        return self.active
    
    def get_id(self):
        return self.id_
    
    def deactivate(self):
        self.active = False
       

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def make_grid(lines):
    rows = len(lines)
    cols = len(lines[0])
    grid = {}
    for y, line in enumerate(lines):
        for x, val in enumerate(line):
                grid[P(x,y)] = val
    return rows,cols,grid


def fire_beam(grid, beam):
    nrg = set()
    while beam.get_active():
        cpos = beam.get_pos()
        if cpos in grid:
            val = grid[cpos]
            #print_grid(grid)
            if val in ('/', '\\'):
                beam.move_mirror(val)
                nrg.add(cpos)
            elif val in ('|', '-'):
                npos,ndir = beam.move_splitter(val, cpos)
                if ndir != 0:
                    nrg.update(fire_beam(grid, Beam(npos, ndir)))
                nrg.add(cpos)
            elif val == '.':
                beam.move_empty()
                nrg.add(cpos)
                grid[cpos] = beam.get_dir()
            else: 
                beam.move_trav(val)
                nrg.add(cpos)
        else:
            beam.deactivate()
    return nrg

def print_grid(grid):
    for y in range(10):
        for x in range(10):
            if grid[P(x,y)] == P(1,0): print('>', end='')
            elif grid[P(x,y)] == P(-1,0): print('<', end='')
            elif grid[P(x,y)] == P(0,1): print('V', end='')
            elif grid[P(x,y)] == P(0,-1): print('^', end='')
            else: print(grid[P(x,y)], end='')
        print('\n')
    print('_'*40)
    print('\n')


def main():
    lines = read_input("input.txt")
    rows,cols,grid = make_grid(lines)
    nrg = fire_beam(grid.copy(), Beam(P(0,0), P(1,0)))
    p1 = len(nrg)
    print(p1)
    p2 = set()
    for x in range(cols):
        p2.add(len(fire_beam(grid.copy(), Beam(P(x,0), P(0,1)))))
        p2.add(len(fire_beam(grid.copy(), Beam(P(x,rows-1), P(0,-1)))))
    for y in range(rows):
        p2.add(len(fire_beam(grid.copy(), Beam(P(0,y), P(1,0)))))
        p2.add(len(fire_beam(grid.copy(), Beam(P(cols-1,y), P(-1,0)))))
    print(max(p2))


    

if __name__ == "__main__":
    main()