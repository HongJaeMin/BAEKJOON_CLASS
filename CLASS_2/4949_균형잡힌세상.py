# Incomplete
import sys, re
input = sys.stdin.readline

while True:
    inp = input().lower().strip('\n')

    cond = {'(', ')', '[', ']', ' '}
    if any(a in inp for a in cond):
        inp_re = re.sub(r'[a-z ]', '', inp)
        condd = {'()', '[]'}
        while any(a in inp_re for a in condd):
            for a in condd:
                if a in inp_re:
                    inp_re = inp_re.replace(a, '')

        if inp_re == '.':
            print('yes')
        else:
            print('no')
    else:
        break