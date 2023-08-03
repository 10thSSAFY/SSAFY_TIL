# Ladder1
import sys
sys.stdin = open('input_Ladder1.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    for i in arr[99]:
        if i == 2:
            c = cnt
            break
        cnt += 1
    
    r = 99
    
    while r > 0:
        if 0 <= c-1 and arr[r][c-1] == 1:
            while True:
                c -= 1
                if 0 <= c-1 and arr[r][c-1] == 1:
                    continue
                else:
                    r -= 1
                    break

        elif c+1 < 100 and arr[r][c+1] == 1:
            while True:
                c += 1
                if c+1 < 100 and arr[r][c+1] == 1:
                    continue
                else:
                    r -= 1
                    break
        else:
            r -= 1

    print(f'#{tc} {c}')
