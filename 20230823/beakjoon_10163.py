# 색종이
import sys
sys.stdin = open('res/input_beakjoon_10163.txt', 'r')

arr = [[0]*1001 for _ in range(1001)]
N = int(input())
min_x = 1001
min_y = 1001
max_x = 0
max_y = 0
for k in range(1, N+1):
    x, y, w, h = map(int, input().split())
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x+w)
    max_y = max(max_y, y+h)
    for r in range(y, y+h):
        arr[r][x:(x+w)] = [k]*w

for k in range(1, N+1):
    cnt = 0
    for r in range(min_y, max_y):
        cnt += arr[r][min_x:max_x].count(k)
    print(cnt)
