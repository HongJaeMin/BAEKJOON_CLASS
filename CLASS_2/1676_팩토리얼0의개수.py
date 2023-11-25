import sys, math

input = sys.stdin.readline
N = int(input().strip())
N_list = list(str(math.factorial(N)))[::-1]

total = 0
for i in N_list:
    if int(i) + 1 == 1:
        total += 1
    else:
        break
print(total)