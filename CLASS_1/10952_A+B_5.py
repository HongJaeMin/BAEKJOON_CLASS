import sys

A = 1
B = 1
while A + B != 0:
    A, B = map(int, sys.stdin.readline().split())
    if A + B != 0:
        print(A + B)
    else:
        break