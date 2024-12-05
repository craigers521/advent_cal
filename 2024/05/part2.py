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


def sort_correctly(pages, rules):
    while True:
        is_sorted = True
        for i in range(len(pages) - 1):
            # Out of order?
            if [pages[i+1], pages[i]] in rules:
                is_sorted = False
                pages[i], pages[i+1] = pages[i+1], pages[i]
        
        if is_sorted:
            return pages

def find_middle_sort(bad_pages, rules):
    ans = 0
    for page in bad_pages:
        sorted = sort_correctly(page, rules)
        ans += sorted[len(sorted) // 2]
    return ans


def main():
    lines = read_input("input.txt")
    rules,pages = parse_lines(lines)
    good_pages, bad_pages = find_good(rules, pages)
    ans = find_middle_sort(bad_pages, rules)
    print(ans)

if __name__ == "__main__":
    main()