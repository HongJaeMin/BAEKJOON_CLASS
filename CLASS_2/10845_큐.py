import sys
from collections import deque
input = sys.stdin.readline

def push(X, q):
    q.append(int(X))

def popp(q):
    if not q:
        print(-1)
    else:
        print(q[0])
        q.popleft()

def size(q):
    return len(q)

def empty(q):
    if not q:
        print(1)
    else:
        print(0)

def front(q):
    if not q:
        print(-1)
    else:
        print(q[0])

def back(q):
    if not q:
        print(-1)
    else:
        print(q[-1])

N = int(input())
queue = deque()
for _ in range(N):
    inp = input().split()
    if inp[0] == 'push':
        push(inp[1], queue)
    elif inp[0] == 'pop':
        popp(queue)
    elif inp[0] == 'size':
        print(size(queue))
    elif inp[0] == 'empty':
        empty(queue)
    elif inp[0] == 'front':
        front(queue)
    elif inp[0] == 'back':
        back(queue)