# 에라토스테네스의 체 공부
import sys
input = sys.stdin.readline

def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    else:
        for y in range(2, int(x**0.5)+1):
            if x % y == 0:
                return False
        return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if is_prime(i):
        print(i)