# 자기 방으로 돌아가기
import sys
sys.stdin = open('res/input_4408.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [0] * 201
    for _ in range(N):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        s = (s+1) // 2 if s % 2 == 1 else s // 2
        e = (e+1) // 2 if e % 2 == 1 else e // 2
        for i in range(s, e+1):
            lst[i] += 1
    result = max(lst)
    print(f'#{tc} {result}')
