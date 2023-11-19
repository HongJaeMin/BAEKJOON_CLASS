# H, M = map(int, input().split()) 
# if H == 0 and M < 45:
#     H = 23
#     M = 60 - abs(M - 45)
# elif M >= 45:
#     H = H
#     M -= 45
# elif M < 45:
#     H -= 1
#     M = 60 - abs(M - 45)
# print(H, M)

H, M = map(int, input().split())
if M < 45:
    M += 15
    if H == 0:
        H = 23
    else:
        H -= 1
else:
    H = H
    M -= 45
print(H, M)