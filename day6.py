
f = open('day6.txt','r').read().splitlines()

sum = 0

group_list = []
group = []
for x in f:
    if x != '':
        group.append(x)
    else:
        group_list.append(group)
        group = []
group_list.append(group)

for x in group_list:
    chars = []
    for c in x:
        for char in c:
            if char not in chars:
                chars.append(char)
    sum+=len(chars)
# print(sum)
# ++++++++++++++++
sum2 = 0
for x in group_list:
    sumsum = 0
    chars = {}
    for c in x:
        for char in c:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1
    for z in chars.values():
        if z == len(x):
            sum2+=1
# print(sum2)
