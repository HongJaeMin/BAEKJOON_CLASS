import sys

input = sys.stdin.readline
N = int(input())

L = []
for _ in range(N):
    x, y = map(int, input().split())
    L.append((x, y))

score = []
for i in range(N):
    cnt = 0
    for j in range(N):
        if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
            cnt += 1
    score.append(cnt + 1)
print('\n'.join(map(str, score)))