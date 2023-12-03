import sys
input = sys.stdin.readline

def round_off(X):
    if X - int(X) >= 0.5:
        X = int(X) + 1
    else:
        X = int(X)
    return X

def trimmed_mean(L):
    cond = round_off(len(L) * 0.15)
    L[:cond] = []
    L[-cond:] = []
    X = sum(L) / len(L)
    mean = round_off(X)
    return mean

n = int(input())
n_list = []
for _ in range(n):
    inp = int(input())
    n_list.append(inp)
n_list.sort()

if len(n_list) == 0:
    print(0)
elif len(n_list) <= 3:
    print(round_off(sum(n_list) / len(n_list)))
else:
    print(trimmed_mean(n_list))