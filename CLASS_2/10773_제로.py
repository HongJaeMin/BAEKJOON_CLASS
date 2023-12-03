import sys
input = sys.stdin.readline

K = int(input())
stack = []
while K > 0:
    K = K
    inp = int(input())
    if inp != 0:
        stack.append(inp)
    else:
        stack.pop()
    K -= 1
print(sum(stack))