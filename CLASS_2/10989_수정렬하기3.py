import sys

input = sys.stdin.readline
N = int(input())

L = []
for _ in range(N):
    num = int(input())
    L.append(num)
sorted_list = sorted(L)
print(sorted_list)