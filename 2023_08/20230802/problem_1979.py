# 어디에 단어가 들어갈 수 있을까
import sys
sys.stdin = open('input_1979.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N, M = 5, 3
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for r in range(N):
        line = [0]
        for c in range(N):
            line.append(arr[r][c])
        line.append(0)
        for i in range(N-M+1):
            new_line = line[i : i+M+2]
            if sum(new_line) ==M and new_line[0] == 0 and new_line[-1] == 0:
                cnt += 1

    for c in range(N):
        line = [0]
        for r in range(N):
            line.append(arr[r][c])
        line.append(0)
        for i in range(N-M+1):
            new_line = line[i : i+M+2]
            if sum(new_line) == M and new_line[0] == 0 and new_line[-1] == 0:
                cnt += 1

    result = cnt
    print(f'#{tc} {result}')
