# 원재의 메모리 복구하기
import sys
sys.stdin = open('res/input_1289.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    mem = list(input().strip())
    stack = ['0']
    cnt = 0
    for i in mem:
        if stack[0] != i:
            stack[0] = i
            cnt += 1
    print(f'#{tc} {cnt}')
