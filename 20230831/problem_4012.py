# 요리사
import sys
sys.stdin = open('res/input_4012.txt', 'r')

T = int(input())
T = 1
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tmp = []
    for i in range(N-1):
        for j in range(i+1, N):
            tmp.append(arr[i][j]+arr[j][i])
    print(tmp)
    print(f'#{tc}')