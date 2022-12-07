path = []
dirsize = {}

def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def mkfs(sdout):
    for cmd in sdout:
        if cmd.startswith("$"):
            if cmd.startswith("$ cd"):
                cd = cmd[5:]
                if cd == "..":
                    path.pop()
                else:
                    path.append(cd)
            else: continue
        else:
            file = cmd.split(" ")
            if file[0] == "dir":
                continue
            else:
                update_dirsize(int(file[0]))
    pass


def update_dirsize(size):
    local_path = path.copy()
    for i in range(0,len(local_path)):
        abs = ''.join(local_path)
        if abs in dirsize:
            dirsize[abs] = dirsize[abs]+size
        else:
            dirsize[abs] = size
        local_path.pop()
    pass


def sumdirs(maxsize):
    dirsum = 0
    for k in dirsize:
        if dirsize[k] <= maxsize:
            dirsum = dirsum+dirsize[k]
    return dirsum


def find_delete_dir(total_d, req_free):
    total_used = dirsize['/']
    total_free = total_d - total_used
    del_size = min([dirsize[k] for k in dirsize if dirsize[k]+total_free >= req_free])
    return del_size

def main():
    sdout = read_input('input.txt')
    mkfs(sdout)
    dirsum = sumdirs(100000)
    print(dirsum)
    del_dir = find_delete_dir(70000000, 30000000)
    print(del_dir)

if __name__ == "__main__":
    main()