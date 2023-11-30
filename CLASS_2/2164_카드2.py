import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
queue = deque([i for i in range(1, N+1)])

while 1 < len(queue):
    queue.remove(queue[0])
    queue.append(queue.popleft())
print(queue[0])