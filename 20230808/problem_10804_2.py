# 문자열의 거울상
import sys
sys.stdin = open('res/input_10804.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    my_str = input()
    my_str = my_str[::-1]
    new_str = ''
    for s in my_str:
        if s == 'b':
            new_str += 'd'
        elif s == 'd':
            new_str += 'b'
        elif s == 'p':
            new_str += 'q'
        elif s == 'q':
            new_str += 'p'

    print(f'#{tc} {new_str}')
