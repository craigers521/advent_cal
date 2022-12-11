class Monkey:

    def __init__(self, op, test, testr1, testr2):
        self.op = op
        self.test = test
        self.testr1 = testr1
        self.testr2 = testr2
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def do_op(self):
        x = self.items[0]
        x = eval(self.op)
        self.items[0] = x
    
    def bored(self):
        self.items[0] = self.items[0]//3

    def test_item(self):
        if self.items[0] % self.test == 0:
            return self.testr1
        else:
            return self.testr2
        
mlist = []
mlist.append(Monkey("x*19", 23, 2, 3))
#mlist[0].add_item(79)
#mlist[0].add_item(98)
mlist.append(Monkey("x+6", 19, 2, 0))
#mlist[1].add_item(54)
#print(mlist[0].items)
#print(mlist[1].items)
##mlist[1].do_op()
##mlist[1].bored()
#mpass = mlist[1].test_item()
#mlist[mpass].add_item(mlist[1].items.pop(0))
#print(mlist[0].items)
#print(mlist[1].items)
start = [[79, 98], [54, 65, 75, 74]]
i = 0
for monkey in mlist:
    for item in start[i]:
        monkey.add_item(item)
    i += 1

for monkey in mlist:
    print(monkey.items)





