# 문자열의 거울상
import sys
sys.stdin = open('res/input_10804.txt', 'r')

# T = int(input())
# for tc in range(1, T+1):
#     word = input().strip()
#     word = word[::-1]
#     word = word.replace('b','t').replace('d','b').replace('t','d')
#     word = word.replace('p','t').replace('q','p').replace('t','q')
#     print(f'#{tc} {word}')

T = int(input())
for tc in range(1, T+1):
    word = list(input().strip())
    word = word[::-1]
    for i in range(len(word)):
        if word[i] == 'b':
            word[i] = 'td'
        elif word[i] == 'p':
            word[i] = 'tq'
        elif word[i] == 'd':
            word[i] = 'b'
        elif word[i] == 'q':
            word[i] = 'p'
    for i in range(len(word)):
        if word[i] == 'td':
            word[i] = 'd'
        elif word[i] == 'tq':
            word[i] = 'q'

    print(f'#{tc}', ''.join(word))
