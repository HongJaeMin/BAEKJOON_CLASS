def is_prime(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

N = int(input())
num = list(map(int, input().split()))
if len(num) > N:
    raise ValueError('입력 범위 초과')

sum = 0
for i in num:
    sum += is_prime(i)
print(sum)