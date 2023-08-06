# 회문
import sys
sys.stdin = open('res/input_4861.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]
    
    result = ''
    for r in range(N):
        for c in range(N-M+1):
            my_word = ''
            for d in range(M):
                my_word += words[r][c+d]
            if my_word == my_word[::-1]:
                result = my_word

    for c in range(N):
        for r in range(N-M+1):
            my_word = ''
            for d in range(M):
                my_word += words[r+d][c]
            if my_word == my_word[::-1]:
                result = my_word

    print(f'#{tc} {result}')
