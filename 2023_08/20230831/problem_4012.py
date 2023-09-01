# 요리사
import sys
sys.stdin = open('res/input_4012.txt', 'r')

def SNG(lst):
    res = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            res += arr[lst[i]][lst[j]] + arr[lst[j]][lst[i]]
    return res

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 2147483648
    for i in range(1, 1<<(N-1)):
        G1=[]
        G2=[]
        for j in range(N):
            if i&(1<<j):
                G1.append(j)
            else:
                G2.append(j)
        if len(G1) == N//2:
            result = min(result, abs(SNG(G1)-SNG(G2)))

    print(f'#{tc} {result}')
