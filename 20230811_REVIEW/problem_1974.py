# 스도쿠 검증
import sys
sys.stdin = open('res/input_1974.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    rows = [list(map(int, input().split())) for _ in range(9)]
    columns = [list(x) for x in zip(*rows)]
    boxes = [[rows[r+i][c+j] for i in range(3) for j in range(3)]
             for r in range(0, 9, 3) for c in range(0, 9, 3)]

    result = 1

    for row in rows:
        if len(set(row)) != 9:
            result = 0
            break

    if result == 1:
        for col in columns:
            if len(set(col)) != 9:
                result = 0
                break
        
    if result == 1:
        for box in boxes:
            if len(set(box)) != 9:
                result = 0
                break

    print(f'#{tc} {result}')
