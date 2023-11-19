N = int(input())
if N > 100000:
    raise ValueError('입력 범위 초과')
for i in range(1, N+1):
    print(i)