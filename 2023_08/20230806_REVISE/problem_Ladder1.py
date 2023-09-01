# Ladder1
import sys
sys.stdin = open('res/input_Ladder1.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    for c in range(100):
        if arr[99][c] == 2:
            break
    
    for r in range(99, 0, -1):
        if 0 <= c-1 and arr[r][c-1] == 1:
            while 0 <= c-1 and arr[r][c-1] == 1:
                c -= 1
        elif c+1 < 100 and arr[r][c+1] == 1:
            while c+1 < 100 and arr[r][c+1] == 1:
                c += 1

    print(f'#{tc} {c}')
