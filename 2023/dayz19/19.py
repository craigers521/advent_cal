class Part:

    def __init__(self,x,m,a,s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s

def read_input(filename):
    with open(filename) as file:
        rules,parts = file.read().split('\n\n')
        rules = rules.split()
        parts = parts.split()
    return rules,parts

def make_parts(parts):
    plist = []
    for part in parts:
        x,m,a,s = part.split(',')
        x = int(x[3:])
        m = int(m[2:])
        a = int(a[2:])
        s = int(s[2:-1])
        plist.append(Part(x,m,a,s))
    return plist

def make_rules(rules):
    fdict = {}
    for rule in rules:
        start = rule.find('{')
        fname,rest = rule[0:start],rule[start+1:-1]
        frules = rest.split(',')
        fdict[fname] = frules
    return fdict

def eval_parts(parts,rules):
    A = []
    for part in parts:
        if eval_rules(part,rules):
            A.append(part)
    return A

def eval_rules(part,rules):
    func = 'in'
    pv = {'x': part.x, 'm': part.m, 'a': part.a, 's': part.s}
    while True:
        rule = rules[func]
        for flow in rule:
            success = True
            if ':' in flow:
                cond,res = flow.split(':')
                var = cond[0]
                op = cond[1]
                num = int(cond[2:])
                if op == '>':
                    success = pv[var] > num
                else:
                    success = pv[var] < num
            else: res = flow
            if success:
                if res == 'A': 
                    return True
                if res == 'R':
                    return False
                else:
                    func = res
                    break


def sum_parts(parts):
    ans = 0
    for part in parts:
        ans += part.x + part.m + part.a + part.s
    return ans


def main():
    rules,parts = read_input("input.txt")
    parts_list = make_parts(parts)
    rules_d = make_rules(rules)
    accepted = eval_parts(parts_list,rules_d)
    p1 = sum_parts(accepted)
    print(p1)
    

if __name__ == "__main__":
    main()