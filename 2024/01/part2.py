def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def split_sort(lines):
    left = []
    right = []
    for line in lines:
        l,r = line.split()
        left.append(int(l))
        right.append(int(r))
    left = sorted(left)
    right = sorted(right)
    return left, right

def find_score(left, right):
    scores = []
    for n in left:
        counter = 0
        for x in right:
            if n == x:
                counter += 1
            if x > n:
                break
        scores.append(n*counter)
    return scores



def main():
    lines = read_input("input.txt")
    left,right = split_sort(lines)
    scores = find_score(left, right)
    ans = sum(scores)
    print(ans)
    

if __name__ == "__main__":
    main()