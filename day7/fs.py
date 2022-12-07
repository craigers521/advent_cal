#import pydash
#import json

fs = {}
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
                #item = {file[1]:int(file[0])}
                update_dirsize(int(file[0]))
                #update_fs(item)
    pass

#def update_fs(item):
#    #sep = "."
#    #dp = sep.join(path)
#    old_dict = pydash.get(fs, path)
#    temp_dict = {'temp_key': {}}
#    if old_dict is not None:
#        temp_dict = {'temp_key': old_dict }
#    temp_dict['temp_key'].update(item)
#    pydash.update(fs, path, temp_dict['temp_key'])
#    pass


def update_dirsize(size):
    for i in range(0,len(path)):
        if path[i] in dirsize:
            dirsize[path[i]] = dirsize[path[i]]+size
        else:
            dirsize[path[i]] = size
    pass


def sumdirs(maxsize):
    dirsum = 0
    for k in dirsize:
        if dirsize[k] <= maxsize:
            dirsum = dirsum+dirsize[k]
    return dirsum


def main():
    sdout = read_input('input.txt')
    mkfs(sdout)
    #print(json.dumps(fs, indent=4))
    dirsum = sumdirs(100000)
    print(dirsum)

if __name__ == "__main__":
    main()