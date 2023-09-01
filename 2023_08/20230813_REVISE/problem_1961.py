# 숫자 배열 회전
import sys
sys.stdin = open('res/input_1961.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
 
    lst1 = [[-1] * N for _ in range(N)]
    lst2 = [[-1] * N for _ in range(N)]
    lst3 = [[-1] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            lst1[r][c] = arr[N-1-c][r]
            lst2[r][c] = arr[N-1-r][N-1-c]
            lst3[r][c] = arr[c][N-1-r]
            
    print(f'#{tc}')
    for i in range(N):
        print(''.join(lst1[i]), ''.join(lst2[i]), ''.join(lst3[i]))
