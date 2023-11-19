sentence = input()

if len(sentence) > 1000000:
    raise ValueError('문자열 길이 초과')

print(len(sentence.split()))