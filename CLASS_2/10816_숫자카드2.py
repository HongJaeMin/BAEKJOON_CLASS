# Counter, Dict 공부
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
if len(N_list) > N:
    raise ValueError()
if len(M_list) > M:
    raise ValueError()

cnt = Counter(N_list)
for i in M_list:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')


# 시간 초과
# import sys
# input = sys.stdin.readline

# N = int(input())
# N_list = list(map(int, input().split()))
# M = int(input())
# M_list = list(map(int, input().split()))
# if len(N_list) > N:
#     raise ValueError()
# if len(M_list) > M:
#     raise ValueError()

# output = []
# for i in M_list:
#     cnt = 0
#     for j in N_list:
#         if i == j:
#             cnt += 1
#     print(cnt, end=' ')