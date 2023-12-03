import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    inp = input().rstrip()
    stack = []
    cnt = 0

    for i in inp:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == ')':
                cnt = 1
                print('NO')
                break
            else:
                stack.pop()
    if cnt == 0:
        if not stack:
            print('YES')
        else:
            print('NO')