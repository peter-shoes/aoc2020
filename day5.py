import sys
import math
f = open('day5.txt','r').read().splitlines()

id_list = []
for code in f:
    rc = (0,127,0,7)
    for char in code:
        switch = {
        'B':(((rc[1]-rc[0]+1)//2),0,0,0),
        'F':(0,-((rc[1]-rc[0]+1)//2),0,0),
        'R':(0,0,((rc[3]-rc[2]+1)//2),0),
        'L':(0,0,0,-((rc[3]-rc[2]+1)//2))
        }
        d = switch[char]
        rc = tuple(map(sum,zip(d,rc)))
    switch_too = {
    'B':rc[1],
    'F':rc[0],
    'R':rc[3],
    'L':rc[2],
    }
    row = switch_too[code[6]]
    col = switch_too[code[9]]
    id_iter = row*8+col
    id_list.append(id_iter)
# print(max(id_list))
# +++++++++++++++++++++++
for id in id_list:
    if id+1 not in id_list:
        if id-1 in id_list:
            if id != max(id_list):
                print(id+1)
