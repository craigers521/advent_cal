import pydash
import json

fs = {}
path = []

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
                item = {file[1]:int(file[0])}
                update_fs(item)
    pass

def update_fs(item):
    sep = "."
    dp = sep.join(path)
    old_dict = pydash.get(fs, dp)
    temp_dict = {'temp_key': {}}
    if old_dict is not None:
        temp_dict = {'temp_key': old_dict }
    temp_dict['temp_key'].update(item)
    pydash.update(fs, dp, temp_dict['temp_key'])
    pass


            


def main():
    sdout = read_input('input.txt')
    mkfs(sdout)
    print(json.dumps(fs, indent=4))

if __name__ == "__main__":
    main()