# 숫자카드
import sys
sys.stdin = open('res/input_4834.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = str(input())
    idx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for card in cards:
        idx[int(card)] += 1

    max_num = 0
    how_many = 0
    cnt = 0
    for i in idx:
        if how_many <= i:
            how_many = i
            max_num = cnt
        cnt += 1

    print(f'#{tc} {max_num} {how_many}')
