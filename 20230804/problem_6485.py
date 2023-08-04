# 삼성시의 버스노선
import sys
sys.stdin = open('input_6485.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = [0 for _ in range(5001)]
    
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            arr[i] += 1
    
    P = int(input())
    result = ''
    for _ in range(P):
        C = int(input())
        result += ' '+str(arr[C])

    print(f'#{tc}{result}')
