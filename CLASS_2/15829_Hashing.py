from string import ascii_lowercase

L = int(input())
input = list(map(str, input().lower()))
if len(input) > L:
    raise ValueError('입력 범위 초과')

az = list(ascii_lowercase)
exponent = -1
result = []
for i in input:
    for j in az:
        if i == j:
            a = az.index(i) + 1
            exponent += 1
            b = 31**(exponent)
            elem = a * b
            result.append(elem)
print(sum(result) % 1234567891)