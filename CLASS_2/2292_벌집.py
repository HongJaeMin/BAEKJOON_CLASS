import sys
input = sys.stdin.readline

inp = int(input())
n = 1
for i in range(inp):
    n += i * 6
    if inp <= n:
        print(i+1)
        break

# 메모리 초과
# import sys
# input = sys.stdin.readline

# inp = int(input())
# L = [i for i in range(2, inp+1)]

# n = 1
# while len(L) > 0:
#     if len(L) >= 6 * n:
#         L[:6 * n] = ''
#         n += 1
#     else:
#         n += 1
#         break
# print(n)