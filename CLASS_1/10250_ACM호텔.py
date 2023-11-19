T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    a = N % H
    b = (N // H) + 1
    if a == 0:
        a = H
        b -= 1
    room_number = a * 100 + b
    print(room_number)