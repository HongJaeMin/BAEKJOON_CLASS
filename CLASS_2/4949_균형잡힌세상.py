# 스택 공부
import sys
input = sys.stdin.readline

while True:
    inp = input().rstrip()
    stack = []
    cnt = 0

    if inp == '.':
        break
    for i in inp:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                cnt = 1
                print('no')
                break
            else:
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                cnt = 1
                print('no')
                break
            else:
                stack.pop()
    if cnt == 0:
        if not stack:
            print('yes')
        else:
            print('no')