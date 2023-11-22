N = int(input())
score_list = list(map(int, input().split()))
if len(score_list) > N:
    raise ValueError('입력 범위 초과')
elif len(score_list) < N:
    raise ValueError('입력 범위 미만')
else:
    total = 0
    for i in score_list:
        if i == 0:
            total += 1
    if total == N:
        raise ValueError('모든 값이 0은 아니어야 함')
    else:
        new_score_list = []
        max_score = max(score_list)
        for i in score_list:
            new_score = i / max_score * 100
            new_score_list.append(new_score)
        avg_score = sum(new_score_list) / N
        print(avg_score)