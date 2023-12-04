import sys
from collections import Counter
input = sys.stdin.readline

def mean(L):
    if len(L) == 1:
        return L[0]
    else:
        return int(round(sum(L) / len(L)))

def median(L):
    if len(L) == 1:
        return L[0]
    else:
        cond = len(L) // 2
        if len(L) % 2 == 0:
            return int(round((L[cond-1] + L[cond]) / 2))
        else:
            return int(round(L[cond]))

def mode(L):
    cnt = Counter(L)
    if len(cnt) == 1:
        return cnt.most_common()[0][0]
    else:
        if cnt.most_common()[0][1] == cnt.most_common()[1][1]:
            return cnt.most_common()[1][0]
        else:
            return cnt.most_common()[0][0]
    
def minmax(L):
    if len(L) == 1:
        return 0
    else:
        return int(max(L) - min(L))

N = int(input())
L = []
for _ in range(N):
    inp = int(input())
    L.append(inp)
L.sort()

print(mean(L))
print(median(L))
print(mode(L))
print(minmax(L))