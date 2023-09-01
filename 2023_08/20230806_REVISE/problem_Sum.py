# Sum
import sys
sys.stdin = open('res/input_Sum.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    result = 0
    for r in range(100):
        line_sum = 0
        for c in range(100):
            line_sum += arr[r][c]
        if result < line_sum:
            result = line_sum

    for c in range(100):
        line_sum = 0
        for r in range(100):
            line_sum += arr[r][c]
        if result < line_sum:
            result = line_sum
    
    line_sum = 0
    line_sum2 = 0
    for i in range(100):
        line_sum += arr[i][i]
        line_sum2 += arr[i][99-i]

    if result < line_sum:
        result = line_sum
    if result < line_sum2:
        result = line_sum2

    print(f'#{tc} {result}')
