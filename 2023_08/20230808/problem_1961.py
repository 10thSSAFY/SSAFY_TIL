# 숫자 배열 회전
import sys
sys.stdin = open('res/input_1961.txt', 'r')

T = int(input())

for tc in range(1, T+1) :
 
    n = int(input())
    arr = [[*map(int,input().split())] for _ in range(n)]
     
    print (f'#{tc}')
    
    for k in range(n):
        a = []
        b = []
        c = []
        for j in range(n):
            a.append(str(arr[n-j-1][k]))
            b.append(str(arr[n-k-1][n-j-1]))
            c.append(str(arr[j][n-k-1]))
        A = ''.join(a)
        B = ''.join(b)
        C = ''.join(c)
        print(A, B, C)
