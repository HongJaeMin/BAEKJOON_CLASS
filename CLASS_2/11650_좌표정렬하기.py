import sys

input = sys.stdin.readline
N = int(input())

L = []
for _ in range(N):
    x, y = map(int, input().split())
    L.append([x, y])
L.sort()
for elem in L:
    x, y = elem
    print(x, y)

# 시간 초과
# import sys

# input = sys.stdin.readline
# N = int(input())

# L = []
# for _ in range(N):
#     x, y = map(int, input().split())
#     L.append([x, y])
# L = sorted(L, key=lambda x: x[0])

# for i in range(N):
#     for j in range(i+1, N):
#         if L[i][0] == L[j][0] and L[i][1] > L[j][1]:
#             L[i][1], L[j][1] = L[j][1], L[i][1]
# for elem in L:
#     x, y = elem
#     print(x, y)