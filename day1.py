file = open('day1.txt').read().splitlines()

f = []
for x in file:
    f.append(int(x))

for x in f:
    for y in f:
        if (x+y) == 2020:
            correct = [x,y]

code1 = correct[0]*correct[1]

for x in f:
    for y in f:
        for z in f:
            sum = x+y+z
            if sum == 2020:
                correct2 = [x,y,z]

code2 = correct2[0]*correct2[1]*correct2[2]

print(code2)
