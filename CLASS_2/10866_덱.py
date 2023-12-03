import sys
from collections import deque
input = sys.stdin.readline

def push_front(X, q):
    q.appendleft(int(X))

def push_back(X, q):
    q.append(int(X))

def pop_front(q):
    if not q:
        print(-1)
    else:
        print(q[0])
        q.popleft()

def pop_back(q):
    if not q:
        print(-1)
    else:
        print(q[-1])
        q.pop()

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
    if inp[0] == 'push_front':
        push_front(inp[1], queue)
    elif inp[0] == 'push_back':
        push_back(inp[1], queue)
    elif inp[0] == 'pop_front':
        pop_front(queue)
    elif inp[0] == 'pop_back':
        pop_back(queue)
    elif inp[0] == 'size':
        print(size(queue))
    elif inp[0] == 'empty':
        empty(queue)
    elif inp[0] == 'front':
        front(queue)
    elif inp[0] == 'back':
        back(queue)