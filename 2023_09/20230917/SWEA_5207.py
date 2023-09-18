import sys
sys.stdin = open('res/input_SWEA_5207.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    cnt = 0
    for num in list(map(int, input().split())):
        s, e = 0, N - 1
        tmp = 'None'
        while s <= e:
            middle = (s + e) // 2
            if num > lst[middle] and tmp != 'left':
                s = middle + 1
                tmp = 'left'
            elif num < lst[middle] != 'right':
                e = middle - 1
                tmp = 'right'
            elif num == lst[middle]:
                cnt += 1
                break
            else:
                break

    print(f'#{tc} {cnt}')
