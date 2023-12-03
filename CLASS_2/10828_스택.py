# for문, 함수 정의 O  ->  152ms
import sys
input = sys.stdin.readline

def push(X, stack):
    stack.append(int(X))

def popp(stack):
    if not stack:
        print(-1)
    else:
        print(stack[-1])
        stack.pop()

def size(stack):
    return len(stack)

def empty(stack):
    if not stack:
        print(1)
    else:
        print(0)

def top(stack):
    if not stack:
        print(-1)
    else:
        print(stack[-1])    

N = int(input())
stack = []    
for _ in range(N):
    inp = input().split()
    if inp[0] == 'push':
        push(inp[1], stack)
    elif inp[0] == 'pop':
        popp(stack)
    elif inp[0] == 'size':
        print(size(stack))
    elif inp[0] == 'empty':
        empty(stack)
    elif inp[0] == 'top':
        top(stack)


# while문, 함수 정의 X  ->  168ms
import sys
input = sys.stdin.readline

N = int(input())
stack = []    
while N > 0:
    N = N
    inp = input().split()

    if inp[0] == 'push':
        stack.append(int(inp[1]))
        N -= 1
    elif inp[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
        N -= 1
    elif inp[0] == 'size':
        print(len(stack))
        N -= 1
    elif inp[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
        N -= 1
    elif inp[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
        N -= 1