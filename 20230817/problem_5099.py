# 피자굽기
import sys
sys.stdin = open('res/input_5099.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst_i = [x for x in range(M)]

    stack = []
    for _ in range(N):
        stack.append(lst_i.pop(0))

    while stack:
        if stack and lst[stack[0]] == 0:
            stack.pop(0)
            if lst_i:
                stack.insert(0, lst_i.pop(0))

        if len(stack) == 1:
            break

        else:
            lst[stack[0]] //= 2
            if lst[stack[0]] == 0:
                stack.pop(0)
                if lst_i:
                    stack.insert(0, lst_i.pop(0))
            stack.append(stack.pop(0))
            


    print(f'#{tc} {stack[0]+1}')