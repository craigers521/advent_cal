def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def parse_lines(lines):
    rules = []
    pages = []
    for line in lines:
        try:
            if "|" in line:
                rules.append(list(map(int, line.split("|"))))
            else:
                pages.append(list(map(int, line.split(","))))
        except:
            pass
    return rules, pages

def find_good(rules, pages):
    good_pages = []
    bad_pages = []
    for page in pages:
        temp_stack = [page[0]]
        bad = 0
        for i in range(1, len(page)):
            for rule in rules:
                if page[i] == rule[0] and rule[1] in temp_stack:
                    bad +=1
                    break
            temp_stack.append(page[i])
            if bad > 0:
                break
        if bad == 0:
            good_pages.append(page)
        else: bad_pages.append(page)
    return good_pages, bad_pages


def find_middles(pages):
    ans = 0
    for page in pages:
        middle = int((len(page)-1)/2)
        ans += page[middle]
    return ans

def main():
    lines = read_input("input.txt")
    rules,pages = parse_lines(lines)
    good_pages = find_good(rules, pages)
    ans = find_middles(good_pages)
    print(ans)

if __name__ == "__main__":
    main()