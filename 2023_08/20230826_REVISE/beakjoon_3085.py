# 사탕 게임
import sys
sys.stdin = open('res/input_beakjoon_3085.txt', 'r')
input = sys.stdin.readline

def check(arr):
    global result
    for row in range(N):
        tmp = arr[row][0]
        cnt = 0
        for col in range(N):
            if tmp == arr[row][col]:
                cnt += 1
                if result < cnt:
                    result = cnt
            else:
                tmp = arr[row][col]
                cnt = 1
    for col in range(N):
        tmp = arr[0][col]
        cnt = 0
        for row in range(N):
            if tmp == arr[row][col]:
                cnt += 1
                if result < cnt:
                    result = cnt
            else:
                tmp = arr[row][col]
                cnt = 1


N = int(input())
arr = [list(input().strip()) for _ in range(N)]

result = 0
for r in range(N):
    for c in range(N-1):
        if arr[r][c] != arr[r][c+1]:
            arr[r][c:c+2] = [arr[r][c+1], arr[r][c]]
            check(arr)
            arr[r][c:c+2] = [arr[r][c+1], arr[r][c]]

arr = [list(x) for x in zip(*arr)]
for r in range(N):
    for c in range(N-1):
        if arr[r][c] != arr[r][c+1]:
            arr[r][c:c+2] = [arr[r][c+1], arr[r][c]]
            check(arr)
            arr[r][c:c+2] = [arr[r][c+1], arr[r][c]]

print(result)
