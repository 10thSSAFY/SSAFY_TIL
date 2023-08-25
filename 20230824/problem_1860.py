# Magnetic
import sys
sys.stdin = open('res/input_1860.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    rows = [list(map(int, input().split())) for _ in range(N)]
    cols = [list(x) for x in zip(*rows)]

    cnt = 0
    for col in cols:
        L = 0
        for i in col:
            if i == 1:
                L = 1
            elif i == 2 and L == 1:
                cnt += 1
                L = 2

    print(f'#{tc} {cnt}')
