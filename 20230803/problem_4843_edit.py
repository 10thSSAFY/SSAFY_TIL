# 특별한 정렬
import sys
sys.stdin = open('input_4843.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
 
    cnt = 0
    result = ''
    while cnt < 5:
        result += ' ' + str(lst[-1 - cnt])
        result += ' ' + str(lst[0 + cnt])
        cnt += 1
 
    print(f'#{tc}{result}')
