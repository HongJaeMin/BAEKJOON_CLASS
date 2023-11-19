S = input().lower()
place = 'abcdefghijklmnopqrstuvwxyz'

# for i in place:
#     if i in S:
#         print(S.index(i), end=' ')
#     else:
#         print(-1, end=' ')

for i in place:
    print(S.find(i), end=' ')