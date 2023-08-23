import sys
sys.stdin = open('res/input_beakjoon_10163.txt', 'r')

arr = [[0] * 1001 for _ in range(1001)]

N = int(input())
for i in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for r in range(x, x+w):
        for c in range(y, y+h):
            arr[r][c] = i

for cnt in range(1, N+1):
    result = 0
    for a in arr:
        result += a.count(cnt)
    print(result)