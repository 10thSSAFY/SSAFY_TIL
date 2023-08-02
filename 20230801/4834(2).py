import sys
sys.stdin = open('4834.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = input()  # cards = 49679

    cards_info = {}
    for num in cards:
        if num not in cards_info:
            cards_info[num] = 1
        else:
            cards_info[num] += 1
    # cards_info = {'4': 1, '9': 2, '6': 1, '7': 1}

    sorted_cards_info = sorted(cards_info.items(), reverse=True)
    # sorted_cards_info = [('9', 2), ('7', 1), ('6', 1), ('4', 1)]

    temp = 0
    for info in sorted_cards_info:
        if temp < info[1]:
            temp = info[1]
            max_num = info[0]
            num_count = info[1]

    print(f'#{tc} {max_num} {num_count}')
