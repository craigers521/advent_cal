class Monkey:

    def __init__(self, op, test, testr1, testr2):
        self.op = op
        self.test = test
        self.testr1 = testr1
        self.testr2 = testr2
        self.items = []
        self.seen = 0

    def add_item(self, item):
        self.items.append(item)

    def inspect(self):
        x = self.items[0]
        x = eval(self.op)
        self.items[0] = x
        self.seen += 1
    
    def bored(self):
        self.items[0] = self.items[0] % 96577 

    def test_item(self):
        if self.items[0] % self.test == 0:
            return self.testr1
        else:
            return self.testr2


def add_start(items):
    i = 0
    for monkey in mlist:
        for item in items[i]:
            monkey.add_item(item)
        i += 1


def print_monkeys():
    for monkey in mlist:
        print(monkey.items)


def business(rounds):
    for _ in range(rounds):
        for monkey in mlist:
            for _ in range(len(monkey.items)):
                monkey.inspect()
                monkey.bored()
                mpass = monkey.test_item()
                mlist[mpass].add_item(monkey.items.pop(0))


def find_active():
    activity = []
    for monkey in mlist:
        activity.append(monkey.seen)
    return activity

def find_top_two(alist):
    t1 = max(alist)
    alist.remove(t1)
    t2 = max(alist)
    return [t1, t2]

mlist = []
start_items = [[79, 98], [54, 65, 75, 74], [79, 60, 97], [74]]
mlist.append(Monkey("x*19", 23, 2, 3))
mlist.append(Monkey("x+6", 19, 2, 0))
mlist.append(Monkey("x*x", 13, 1, 3))
mlist.append(Monkey("x+3", 17, 0, 1))

def main():
    add_start(start_items)
    business(20)
    print_monkeys()
    activity = find_active()
    #top2 = find_top_two(activity)
    #print(top2[0]*top2[1])
    activity.sort()
    print(activity[-1]*activity[-2])


if __name__ == "__main__":
    main()


