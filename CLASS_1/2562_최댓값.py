L = []
for i in range(9):
    N = int(input())
    if N >= 100:
        raise ValueError(f'100보다 큰 수를 입력함')
    L.append(N)
print(max(L))
print(L.index(max(L)) + 1)