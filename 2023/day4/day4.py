def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def make_cards(lines):
    tempcards = []
    tempwins = []
    newlines = [line.split(': ')[1] for line in lines]
    for line in newlines:
        x,y = line.split(" | ")
        tempcards.append(x)
        tempwins.append(y)
    cardlist = listcleanup(tempcards)
    winlist = listcleanup(tempwins)
    return cardlist,winlist


def listcleanup(numlist):
    temp = []
    for line in numlist:
        clean = line.split()
        temp.append(clean)
    return temp
    

def findwins(cards, wins):
    points = 0
    for i,card in enumerate(cards):
        counter = 0
        for num in card:
            if num in wins[i]:
                counter += 1
        if counter > 0:
            points += 2**(counter-1)
    return points


def main():
    lines = read_input("input.txt")
    cardlist,winlist = make_cards(lines)
    p1 = findwins(cardlist,winlist)
    print(p1)
    

if __name__ == "__main__":
    main()