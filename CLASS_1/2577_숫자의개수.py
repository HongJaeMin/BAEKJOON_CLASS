num_list = []
for i in range(3):
    num = int(input())
    if num < 100 or num >= 1000:
        raise ValueError('입력 범위 초과')
    else:
        num_list.append(num)

num_times = 1
for i in range(0, len(num_list)):
    num_times *= num_list[i]

times_list = list(map(int, list(str(num_times))))

for i in range(0, 10):
    print(times_list.count(i))