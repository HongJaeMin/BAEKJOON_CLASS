T = int(input())
for _ in range(T):
    problem = list(input().split('X'))
    sum = 0
    for i in range(len(problem)):
        if 'O' in problem[i]:
            for score in range(1, problem[i].count('O')+1):
                sum += score
    print(sum)