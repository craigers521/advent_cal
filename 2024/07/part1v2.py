import math

def read_input(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def build_eqs(lines):
    eqs = []
    for line in lines:
        ans,nums = line.split(": ")
        eqs.append({int(ans): [int(x) for x in nums.split()]})
    return eqs

def find_ops(eqs):
    total = 0
    for eq in eqs:
        for k, v in eq.items():
            if solvable(k, v):
                total += k
    return total
            
def solvable(ans, nums):
    if len(nums) ==1: return ans == nums[0]
    if solvable(ans, [nums[0]+nums[1]] + nums[2:]): return True
    if solvable(ans, [nums[0]*nums[1]] + nums[2:]): return True
    if solvable(ans, [int(str(nums[0])+str(nums[1]))] + nums[2:]): return True
    return False


def main():
    lines = read_input("input.txt")
    eqs = build_eqs(lines)
    ans = find_ops(eqs)
    print(ans)
    

if __name__ == "__main__":
    main()