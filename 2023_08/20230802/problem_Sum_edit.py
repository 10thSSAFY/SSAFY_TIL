# Sum
import sys
sys.stdin = open('input_Sum.txt', 'r')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for r in range(100):
        tmp = 0
        for c in range(100):
            tmp += arr[r][c]
        if result < tmp:
            result = tmp
    
    for c in range(100):
        tmp = 0
        for r in range(100):
            tmp += arr[r][c]
        if result < tmp:
            result = tmp

    tmp, tmp2 = 0, 0
    for i in range(100):
        tmp += arr[i][i]
        tmp2 += arr[i][99-i]
    
    if tmp > result and tmp > tmp2:
        result = tmp
    elif tmp2 > result:
        result = tmp2
        
    print(f'#{tc} {result}')
