def read_input(filename):
    lines = []
    with open(filename) as file:
        temp_list =[]
        for line in file:
            line = line.rstrip()
            if line != "":
                temp_list.append(line)
            else:
                lines.append(temp_list.copy())
                temp_list.clear()
    return lines


def sum_lists(elves):
    sum_list =[]
    for elf in elves:
        elf = list(map(int, elf))
        sum_list.append(sum(elf))
    return sum_list


def main():
    elf_bags = read_input('input.txt')
    total_cals = sum_lists(elf_bags)
    max_cals = max(total_cals)
    print(f"The highest calorie is {max_cals}")
    total_cals.sort(reverse=True)
    top3 = sum(total_cals[:3])
    print(f"Sum of top 3 is {top3}")


if __name__ == "__main__":
    main()


