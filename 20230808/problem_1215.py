# 회문 1
import sys
sys.stdin = open('res/input_1215.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    words = [input() for _ in range(8)]

    cnt = 0
    for word in words:
        for i in range(8-N+1):
            new_word = word[i:i+N]
            if new_word == new_word[::-1]:
                cnt += 1

    for n in range(8):
        new_str = ''
        for word in words:
            new_str += word[n]
        for i in range(8-N+1):
            new_word = new_str[i:i+N]
            # print(new_word)
            if new_word == new_word[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')
