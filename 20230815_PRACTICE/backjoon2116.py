# 주사위 쌓기
import sys
sys.stdin = open('res/input_backjoon2116.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
pair = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
result = 0
for bottom in range(1, 7):
    max_sum = 0
    for r in range(N):
        dice = arr[r]
        top = dice[pair[dice.index(bottom)]]
        temp = [1, 2, 3, 4, 5, 6]
        temp.remove(top)
        temp.remove(bottom)
        max_sum += max(temp)
        bottom = top
    if result < max_sum:
        result = max_sum

print(result)
