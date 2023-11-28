import sys

input = sys.stdin.readline
N = int(input())

L = []
for _ in range(N):
    x, y = map(int, input().split())
    L.append([x, y][::-1])
L.sort()
for elem in L:
    x, y = elem[::-1]
    print(x, y)