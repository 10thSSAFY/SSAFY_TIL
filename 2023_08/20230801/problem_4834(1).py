# 숫자카드
import sys
sys.stdin = open('input_4834.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = input()                     # cards = 49679
    cards_idx = [0] * 10                # cards_idx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for num in cards:
        cards_idx[int(num)] += 1        # cards_idx = [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    num_count = max(cards_idx)          # num_count = 2

    cards_idx.reverse()
    temp = cards_idx.index(num_count)
    max_num = 9 - temp                  # max_num = 9

    print(f'#{tc} {max_num} {num_count}')