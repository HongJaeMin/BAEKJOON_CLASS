import sys

input = sys.stdin.readline
N = int(input().strip())

num_list = []
for _ in range(N):
    nums = int(input().strip())
    num_list.append(nums)
num_list = sorted(list(set(num_list)))

# 908 ms
for num in num_list:
    print(num)

# 720 ms
print('\n'.join(map(str, num_list)))