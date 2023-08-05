# view
import sys
sys.stdin = open('res/input_view.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    result = 0
    for idx in range(2, N-2):
        views = [lst[idx] - lst[idx-2], lst[idx] - lst[idx-1], lst[idx] - lst[idx+1], lst[idx] - lst[idx+2]]
        result_view = 256
        for view in views:
            if view <= 0:
                result_view = 0
                break
            elif result_view > view:
                result_view = view
        result += result_view
        
    print(f'#{tc} {result}')
