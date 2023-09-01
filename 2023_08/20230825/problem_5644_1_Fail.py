# 무선충전
import sys
sys.stdin = open('res/input_5644.txt')

walk_dir = {0: (0,0), 1: (-1,0), 2: (0,1), 3:(1,0), 4:(0,1)}

T = int(input())
T = 1
for tc in range(1, T+1):
    M, A = map(int, input().split())  # M: 이동 시간, A: BC 개수
    A_walk = list(map(int, input().split()))
    B_walk = list(map(int, input().split()))
    arr = [[[]] * 11 for _ in range(11)]

    for _ in range(A):
        r_pos, c_pos, C, P = map(int, input().split())
        stack = []
        for r in range(-C, C+2):
            for c in range(-C, C+2):
                if abs(r)+abs(c) <= C:
                    stack.append((r, c))

        for dr, dc in stack:
            newR, newC = r_pos+dr, c_pos+dc
            if 1 <= newR < 11 and 1 <= newC < 11:
                ######### arr[newR][newC] = P
                pass

    for line in arr:
        print(line)
    print(f'#{tc}')
