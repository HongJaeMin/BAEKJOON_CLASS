import sys

input = sys.stdin.readline
A, B, V = map(int, input().split())

if (V - B) % (A - B) == 0:
    day = (V - B) // (A - B)
elif (V - B) % (A - B) != 0:
    day = (V - B) // (A - B) + 1
print(day)

# 시간 초과
# day = 0
# while True:
#     day += 1
#     V = V - (A - B)
#     if V <= A:
#         day += 1
#         break
# print(day)