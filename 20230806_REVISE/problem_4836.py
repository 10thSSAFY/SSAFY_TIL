# 색칠하기
import sys
sys.stdin = open('res/input_4836.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                arr[r][c] += color

    cnt = 0
    for i in arr:
        for j in i:
            if j == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
