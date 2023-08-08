# 회문
import sys
sys.stdin = open('res/input_4861.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = [input().strip() for _ in range(N)]

    result = ''
    for word in words:
        for i in range(N-M+1):
            my_word = word[i:i+M]
            if my_word == my_word[::-1]:
                result = my_word

    for n in range(N):
        word = ''.join(list(zip(*words))[n])
        for i in range(N-M+1):
            my_word = word[i:i+M]
            if my_word == my_word[::-1]:
                result = my_word

    print(f'#{tc} {result}')
