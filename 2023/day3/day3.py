def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def find_parts(lines):
    total = 0
    temp_str = ''
    for n,line in enumerate(lines):
        for i,c in  enumerate(line):
            if c.isdigit():
                temp_str = temp_str + c
                if i+1 == len(line):
                     if valid_part(lines,n,i+1,len(temp_str)):
                         total += int(temp_str)
                         temp_str = ''
            elif len(temp_str) > 0 and valid_part(lines,n,i,len(temp_str)):
                total += int(temp_str)
                temp_str = ''
            else:
                temp_str = ''
    return total


def valid_part(lines, line_num, pos, leng):
    if line_num > 0:
        if pos-leng <= 0:
            above = lines[line_num-1][pos-leng:pos+1].replace('.', '')
        else:
            above = lines[line_num-1][pos-leng-1:pos+1].replace('.', '')
        if len(above) > 0:
            if not above.isalnum():
                return True
    if pos-leng > 0:
        left = lines[line_num][pos-leng-1].replace('.','')
        if len(left) > 0:
            if not left.isalnum():
                return True
    if pos < len(lines[line_num]):
        right = lines[line_num][pos].replace('.','')
        if len(right) > 0:
            if not right.isalnum():
                return True
    if line_num+1 < len(lines):
        if pos-leng <= 0:
            below = lines[line_num+1][pos-leng:pos+1].replace('.','')
        else:
            below = lines[line_num+1][pos-leng-1:pos+1].replace('.','')
        if len(below) > 0:
            if not below.isalnum():
                return True
    return False 



def main():
    lines = read_input("input.txt")
    part_total = find_parts(lines)
    print(part_total)
    

if __name__ == "__main__":
    main()