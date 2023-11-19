T = int(input())
for _ in range(0, T):
    S = input().split()
    S_list = list(S[1])
    P = []
    for i in range(0, len(S_list)):
        S_list[i] = S_list[i] * int(S[0])
        P.append(S_list[i])
    print(''.join(P))