import sys

input = sys.stdin.readline
N = int(input())

L = [0] * 10001
for _ in range(N):
    num = int(input())
    L[num] += 1
for i in range(0, len(L)):
    if L[i] != 0:
        for _ in range(L[i]):
            print(i)

# 메모리 초과
# L = []
# for _ in range(N):
#     num = int(input())
#     L.append(num)
# sorted_list = sorted(L)  # L.sort()
# print(sorted_list)  # print(L)