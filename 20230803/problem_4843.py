# 특별한 정렬
import sys
sys.stdin = open('input_4843.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    
    sorted_lst = []
    while True:

        if lst and len(sorted_lst) < 10:
            sorted_lst.append( str(lst.pop(lst.index(max(lst)))) )
        else:
            break

        if lst and len(sorted_lst) < 10:
            sorted_lst.append( str(lst.pop(lst.index(min(lst)))) )
        else:
            break
    
    result = (' '.join(sorted_lst))
    print(f'#{tc} {result}')
