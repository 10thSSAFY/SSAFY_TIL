# 스도쿠 검증
import sys
sys.stdin = open('res/input_1974.txt', 'r')

corr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in arr:
        if corr != sorted(i):
            result = 0
            break

    while result == 1:
        for c in range(9):
            l = []
            for r in range(9):
                l.append(arr[r][c])
            if corr != sorted(l):
                result = 0
                break
        break

    while result == 1:
        for r in range(0, 9, 3):
            if result == 1:
                for c in range(0, 9, 3):
                    l = []
                    for i in range(3):
                        for j in range(3):
                            l.append(arr[r+i][c+j])
                    if corr != sorted(l):
                        result = 0
                        break
            else:
                break
        break

    print(f'#{tc} {result}')
