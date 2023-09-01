# min max
import sys
sys.stdin = open('res/input_4828.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    max_num = 0
    min_num = 1000001
    for num in lst:
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num
    result = max_num - min_num
    
    print(f'#{tc} {result}')
