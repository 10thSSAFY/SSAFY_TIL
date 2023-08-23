import sys
sys.stdin = open('res/input_beakjoon_2563.txt', 'r')
input = sys.stdin.readline

arr = [[0] * 101 for _ in range(101)]
N = int(input())
x_min = 100
x_max = 0
y_min = 100
y_max = 0
for _ in range(N):
    x, y = map(int, input().split())
    x_min = min(x_min, x)
    y_min = min(y_min, y)
    x_max = max(x_max, x+10)
    y_max = max(y_max, y+10)
    for r in range(y, y+10):
        arr[r][x:x+10] = [1] * 10

result = 0
for line in arr:
    result += sum(line)

print(result)
