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