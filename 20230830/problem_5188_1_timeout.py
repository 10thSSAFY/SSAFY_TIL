# 최소합 (시간 초과)
import sys
sys.stdin = open('res/input_5188.txt', 'r')

def go(delta):
    r, c = 0, 0
    sumV = arr[r][c]
    for dr, dc in delta:
        newR, newC = r+dr, c+dc
        sumV += arr[newR][newC]
        r = newR
        c = newC
    return sumV

def permute(k):
    global result
    if k == len(direction):
        # print(bit)
        delta = []
        for i in range(len(bit)):
            pos = bit[i]
            delta.append(direction[pos])
        result = min(result, go(delta))

    for i in range(len(direction)):
        if not used[i]:
            used[i] = True
            bit[k] = i
            permute(k+1)
            used[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    direction = []
    for _ in range(N-1):
        direction.append((1,0))
    for _ in range(N-1):
        direction.append((0,1))

    used = [False] * len(direction)
    bit = [-1] * len(direction)
    result = 2147483648
    permute(0)
    print(f'#{tc} {result}')
