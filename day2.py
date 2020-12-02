import re
f = open('day2.txt','r').read().splitlines()

count = 0
count2 = 0
for x in f:
    x = x.split(':')
    search_str = x[1].strip()
    match_char = x[0].split(' ')[1]
    match_nums = x[0].split(' ')[0].split('-')
    low = int(match_nums[0])
    high = int(match_nums[1])
    # this is a really shitty way of doing this
    all = re.findall(match_char,search_str)
    if (low<=len(all)<=high):
        count+=1

    c1 = search_str[low-1] == match_char
    c2 = search_str[high-1] == match_char
    if (c1 and not c2) or (not c1 and c2):
        count2 +=1

print(count2)
