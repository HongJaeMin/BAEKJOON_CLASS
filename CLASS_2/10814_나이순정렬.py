import sys

input = sys.stdin.readline
N = int(input())

L = []
for _ in range(N):
    age, name = input().strip().split()
    L.append([int(age), name])

sorted_L = sorted(L, key=lambda x: x[0])
for x, y in sorted_L:
    print(x, y)


# 시간 초과
# import sys

# input = sys.stdin.readline
# N = int(input())

# L = []
# for _ in range(N):
#     age, name = input().strip().split()
#     L.append((int(age), name))

# for i in range(N):
#     for j in range(N):
#         if L[i][0] < L[j][0]:
#             temp = L[i]
#             L.remove(L[i])
#             L.insert(0, temp)
# for x in range(N):  # for x, y in L:
#     age, name = L[x]  # print(x, y)
#     print(age, name)