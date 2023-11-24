import sys

input = sys.stdin.readline
N, K = map(int, input().split())

x = y = z = 1
for i in range(1, (N - K) + 1):
    x *= i
for i in range(1, K + 1):
    y *= i
for i in range(1, N + 1):
    z *= i
print(int(z / (x * y)))


# math 모듈
import math
print(math.comb(N, K))