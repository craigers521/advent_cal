def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def make_cards(lines):
    tempcards = [ ]
    tempwins = [ ]
    newlines = [line.split(': ')[1] for line in lines]
    for line in newlines:
        x,y = line.split(" | ")
        tempcards.append(x)
        tempwins.append(y)
    cardlist = listcleanup(tempcards)
    winlist = listcleanup(tempwins)
    return cardlist,winlist


def listcleanup(numlist):
    temp = { }
    for i,line in enumerate(numlist):
        clean = line.split()
        temp[i+1] = [clean]
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


def make_copies(cardlist,winlist):
    counter = 0
    for key in cardlist:
        for card in cardlist[key]:
            copies = findmatches(card,winlist[key])
            if copies > 0:
                for i in range(copies):
                    cardlist[key+i+1].append(cardlist[key+i+1][0])
            counter += 1
    return counter 
    


def findmatches(card, win):
    counter = 0
    for num in card:
        if num in win[0]:
            counter += 1
    return counter


def main():
    lines = read_input("input.txt")
    cardlist,winlist = make_cards(lines)
    p2 = make_copies(cardlist,winlist)
    print(p2)
    

if __name__ == "__main__":
    main()