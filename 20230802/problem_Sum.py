# Sum
import sys
sys.stdin = open('input_Sum.txt', 'r')

for _ in range(10):
    tc = int(input())

    arr = []
    for _ in range(100):
        lst = list(map(int, input().split()))
        arr.append(lst)
    
    max_row = []
    for i in range(100):
        max_row.append(sum(arr[i]))

    max_col = [0 for _ in range(100)]
    for j in range(100):
        for i in range(100):
            max_col[j] += arr[i][j]

    max_cross = [0, 0]
    for i in range(100):
        max_cross[0] += arr[i][i]
        max_cross[1] += arr[i][-1-i]
    
    result = max(max(max_row), max(max_col), max(max_cross))
    print(f'#{tc} {result}')
