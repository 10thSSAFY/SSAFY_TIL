# 파리 퇴치
import sys
sys.stdin = open('input_2001.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N, M = 5, 2
    
    arr = []
    for _ in range(N):
        line = list(map(int, input().split()))
        arr.append(line)
    
    scores = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            score = 0
            for di in range(M):
                for dj in range(M):
                    score += arr[i+di][j+dj]
            scores.append(score)
    
    result = max(scores)
    print(f'#{tc} {result}')
