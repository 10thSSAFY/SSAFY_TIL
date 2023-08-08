# 스도쿠 검증
import sys
sys.stdin = open('res/input_1974.txt', 'r')

corr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
boxr = [0, 0, 0, 1, 1, 1, 2, 2, 2]
boxc = [0, 1, 2, 0, 1, 2, 0, 1, 2]

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    cnt = 0

    for line in arr:
        if corr == sorted(line):
            cnt += 1
    
    for c in range(9):
        line = []
        for r in range(9):
            line.append(arr[r][c])
        if corr == sorted(line):
            cnt += 1

    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            line = []
            for d in range(9):
                line.append(arr[r+boxr[d]][c+boxc[d]])
            if corr == sorted(line):
                cnt += 1
    
    result = 0
    if cnt == 27:
        result = 1
        
    print(f'#{tc} {result}')
