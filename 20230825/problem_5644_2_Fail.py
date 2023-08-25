# 무선충전
import sys
sys.stdin = open('res/input_5644.txt')

walk_dir = {0: (0,0), 1: (0,-1), 2: (1,0), 3:(0,1), 4:(-1,0)}

T = int(input())
T = 1
for tc in range(1, T+1):
    M, A = map(int, input().split())  # M: 이동 시간, A: BC 개수
    A_walk = list(map(int, input().split()))
    B_walk = list(map(int, input().split()))

    BC_pos = []
    for _ in range(A):
        r_pos, c_pos, C, P = map(int, input().split())
        BC_pos.append((r_pos, c_pos, C, P))

    print(BC_pos)
    Ar, Ac = 1, 1
    Br, Bc = 10, 10
    A_charge = []
    B_charge = []
    tmpA = []
    tmpB = []
    for dr, dc, C, P in BC_pos:
        if abs(Ar-dr)+abs(Ac-dc) <= C:
            tmpA.append(P)
            tmpA.append((dr, dc))
        if abs(Br-dr)+abs(Bc-dc) <= C:
            tmpB.append(P)
            tmpB.append((dr, dc))
    print(tmpA)
    print(tmpB)

    for i in range(0, M):
        dr, dc = walk_dir[A_walk[i]]
        Ar, Ac = Ar+dr, Ac+dc
        print('A:', Ar, Ac)
        dr, dc = walk_dir[B_walk[i]]
        Br, Bc = Br+dr, Bc+dc
        print('B:', Br, Bc)


    print(f'#{tc}')
