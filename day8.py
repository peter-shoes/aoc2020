import sys

def switcher(instr):
    if instr == 'jmp':
        return 'nop'
    elif instr == 'nop':
        return 'jmp'
    else:
        print('exit')
        sys.exit(0)

def mainrun(f):
    acc = 0

    ran = []

    index = 0
    iterator = 0
    while index < len(f):
        instruction = f[index][0]
        val = int(f[index][1])
        if index in ran:
            return False
        ran.append(index)
        if instruction == 'acc':
            acc += val
            index += 1
        elif instruction == 'jmp':
            index += val
        else:
            index += 1
            pass
    return acc

def recur(f):
    for i in f:
        if i[0] == ('jmp' or 'nop'):
            i[0] = switcher(i[0])
            if mainrun(f) != False:
                print(mainrun(f))
            else:
                i[0] = switcher(i[0])

def main():
    f = open('day8.txt','r').read().splitlines()
    f = [i.strip().split(' ') for i in f]
    recur(f)

if __name__ == '__main__':
    main()
