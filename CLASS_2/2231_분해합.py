N = int(input())

N_list = []
M_list = []
for i in range(1, N+1):
    M_list.append(str(i))
    if len(str(i)) == 1:
        N_list.append(i*2)
    else:
        a = sum(list(map(int, list(str(i)))))
        N_list.append(i + a)

if N in N_list:
    idx = N_list.index(N)
    print(M_list[idx])
else:
    print(0)