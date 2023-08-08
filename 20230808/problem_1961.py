# 숫자 배열 회전
import sys
sys.stdin = open('res/input_1961.txt', 'r')

T = int(input())

for i in range(1, T+1) :
 
    n = int(input())
    arr = [[*map(int,input().split())] for _ in range(n)]
     
    print ('#{}'.format(i))
    a = []
    b = []
    c = []
    for k in range(n):
        for j in range(n):
            a.append(arr[n-j-1][k])
            b.append(arr[n-k-1][n-j-1])
            c.append(arr[j][n-k-1])
        a = list(map(str, a))
        b = list(map(str, b))
        c = list(map(str, c))
        A = ''.join(a)
        B = ''.join(b)
        C = ''.join(c)
        print(A, B, C)
        a = []
        b = []
        c = []