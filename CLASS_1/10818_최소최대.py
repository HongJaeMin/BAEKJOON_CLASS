import sys

N = int(input())
L = list(map(int, sys.stdin.readline().split()))
if len(L) > N:
    raise ValueError(f'{N}개 이상의 정수가 입력됨')
print(min(L), max(L))