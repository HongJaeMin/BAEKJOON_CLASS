from itertools import combinations

N, M = map(int, input().split())
card_list = list(map(int, input().split()))
if len(card_list) > N:
    raise ValueError('입력 범위 초과')

card_comb_list = list(combinations(card_list, 3))
result = []
for card_comb in card_comb_list:
    if sum(card_comb) <= M:
        result.append(sum(card_comb))
print(max(result))