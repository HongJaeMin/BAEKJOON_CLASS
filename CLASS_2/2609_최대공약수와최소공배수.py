def gcd_lcm(x, y):
    total = 1
    i = 2
    while i <= 10000:
        while x % i == 0 and y % i == 0:
            total *= i
            x = x // i
            y = y // i
        i += 1
        
    gcd = total
    lcm = gcd * x * y
    return gcd, lcm

A, B = map(int, input().split())
output1, output2 = gcd_lcm(A, B)
print(output1)
print(output2)


# 유클리드 호제법
def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return int(x * y / gcd(x, y))

A, B = map(int, input().split())
if A < B:
    A, B = B, A
result1 = gcd(A, B)
result2 = lcm(A, B)
print(result1)
print(result2)