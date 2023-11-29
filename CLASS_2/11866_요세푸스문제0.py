# deque 공부
import sys
from collections import deque

input = sys.stdin.readline

queue = deque()
N, K = map(int, input().split())
for i in range(1, N+1):
    queue.append(i)

output = []
while len(queue) > 0:
    for _ in range(K-1):
        K_popleft = queue.popleft()
        queue.append(K_popleft)
    output.append(queue.popleft())
print(f"<{', '.join(map(str, output))}>")