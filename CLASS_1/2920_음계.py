N = list(map(int, input().split()))

ascending = sorted(N)
descending = sorted(N, reverse=True)

if N == ascending:
    print('ascending')
elif N == descending:
    print('descending')
else:
    print('mixed')