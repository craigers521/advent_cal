from collections import defaultdict

lines = [10,20,30,40,50,60,70,80,90]
N = defaultdict(int)
for i,line in enumerate(lines):
    N[i] +=1
    for j in range(5):
        N[i+1+j] += N[i]
print(sum(N.values()))
