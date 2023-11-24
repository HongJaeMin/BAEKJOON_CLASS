while True:
    N = int(input())
    if N == 0:
        break
    else:
        N_list = list(str(N))
        cond = len(N_list) // 2
        if len(N_list) % 2 == 1:
            left_N = N_list[:cond]
            right_N = N_list[cond+1:][::-1]
        elif len(N_list) % 2 == 0:
            left_N = N_list[:cond]
            right_N = N_list[cond:][::-1]
        if left_N == right_N:
            print('yes')
        else:
            print('no')