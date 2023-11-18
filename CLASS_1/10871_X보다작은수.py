import sys

N, X = map(int, input().split())
L = list(map(int, sys.stdin.readline().split()))
if len(L) > N:
    raise ValueError('입력한 정수의 개수가 N보다 큼')
i_list = []
for i in L:
    if i < X:
        i_list.append(i)
        print(i, end=' ')