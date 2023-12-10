import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    f0 = [_ for _ in range(1, n+1)]
    i = 0
    while i < k:
        fn = []
        j = 0
        while j < n:
            fn.append(sum(f0[:j+1]))
            j += 1
        f0 = fn
        i += 1
    print(fn[n-1])