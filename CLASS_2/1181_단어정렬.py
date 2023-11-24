import sys

input = sys.stdin.readline
N = int(input())

word_list = []
len_word_list = []
for _ in range(N):
    words = str(input().lower().strip())
    word_list.append(words)
word_list = sorted(list(set(word_list)))

for word in word_list:
    len_word_list.append(len(word))
len_word_list = sorted(len_word_list)

for len_word in len_word_list:
    for word in word_list:
        if len(word) == len_word:
            print(word)
            word_list.remove(word)
            break

# 숏코딩 버전
import sys

input = sys.stdin.readline
N = int(input())

word_list = []
for _ in range(N):
    words = str(input().lower().strip())
    word_list.append(words)
word_list = list(set(word_list))

word_list.sort()
word_list.sort(key=len)
for word in word_list:
    print(word)