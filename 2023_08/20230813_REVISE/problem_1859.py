# 백만 장자 프로젝트
import sys
sys.stdin = open('res/input_1859.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    top = lst[-1]
    result = 0
    for i in range(N-1, -1, -1):
        if top < lst[i]:
            top = lst[i]
        else:
            result += top - lst[i]

    print(f'#{tc} {result}')
