# 고대 유적
import sys
sys.stdin = open('res/input_9489.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(N)]
    # columns = [list(x) for x in zip(*lst)]
    lst.extend([list(x) for x in zip(*lst)])

    result = 0
    for data in lst:
        cur_length = 0
        for num in data:
            if num == 1:
                cur_length += 1
                if result < cur_length:
                    result = cur_length
            else:
                cur_length = 0
        
    print(f'#{tc} {result}')
