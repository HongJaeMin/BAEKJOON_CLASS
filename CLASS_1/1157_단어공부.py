alphabet = input().upper()

if len(alphabet) > 1000000:
    raise ValueError('문자열 길이 초과')
else:
    L = list(alphabet)
    unique_alphabet = list(set(L))

cnt_alphabet = []
for i in unique_alphabet:
    cnt_alphabet.append(L.count(i))

sum = 0
for i in cnt_alphabet:
    if max(cnt_alphabet) == i:
        sum += 1
if sum > 1:
    print('?')
else:
    for i in range(0, len(cnt_alphabet)):
        if cnt_alphabet[i] == max(cnt_alphabet):
            print(unique_alphabet[i])