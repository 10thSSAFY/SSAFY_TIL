# 이진수
import sys
sys.stdin = open("res/input_5185.txt", "r")

num = {'A':10, 'B':11, 'C':12,
       'D':13, 'E':14, 'F':15}
 
T = int(input())
for tc in range(1, T+1):
    N, hx = input().split()
    result = ''
    for n in hx:
        if n in 'ABCDEF':
            n = num[n]
        else:
            n = int(n)
 
        for i in range(4):
            if n & (8>>i):
                result += '1'
            else:
                result += '0'
                 
    print(f'#{tc} {result}')