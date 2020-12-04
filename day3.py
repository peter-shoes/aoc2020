import sys

f = open('day3.txt','r').read().split()

def checker(right_check,down_check):
    run_into = []
    down = 0
    right = 0
    while down <= len(f):
        down +=down_check
        right +=right_check
        if right >= len(f[0]):
            right = right-len(f[0])
        if down >= len(f):
            pass
        else:
            try:
                run_into.append(f[down][right])
            except:
                # print(down,right)
                pass
    # print(down,right)
    count = 0
    for x in run_into:
        if x == '#':
            count+=1
    return count

a = checker(1,1)
b = checker(3,1)
c = checker(5,1)
d = checker(7,1)
e = checker(1,2)

print(a*b*c*d*e)
# print(b)
