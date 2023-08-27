# [SW Test 샘플문제] 프로세서 연결하기
# 진행중,
import sys
sys.stdin = open('res/input_1767.txt', 'r')

def forth(r, c):
    delta = [(-1,0), (1,0), (0,-1), (0,1)]
    ans = []
    for d in range(4):
        l = 0
        while True:
            l += 1
            newR, newC = r+delta[d][0]*l, c+delta[d][1]*l
            if 0<=newR<N and 0<=newC<N and arr[newR][newC] == 0:
                if newR == 0 or newC == 0 or newR == N-1 or newC == N-1:
                    ans.append((newR, newC))
                    break
                else:
                    continue
            else:
                break
    return ans


def mexinous(k):
    global result
    if k == len(S):
        return

    r, c = S[k]
    forth_result = forth(r, c)
    result.append(forth_result)
    mexinous(k+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    S = []
    for r in range(N):
        for c in range(N):
            if r != 0 and c != 0 and r != N-1 and c != N-1 and arr[r][c] == 1:
                S.append((r, c))
    # print(S)  # [(1, 2), (2, 5), (4, 1), (4, 3), (5, 1)]

    result =[]
    mexinous(0)
    # print(result)  # [[(6, 2), (1, 0), (1, 6)], [(0, 5), (6, 5), (2, 0), (2, 6)], [(0, 1)], [(0, 3), (6, 3), (4, 6)], [(6, 1), (5, 0), (5, 6)]]
    for i in range(len(S)):
        r, c = S[i]
        for j in range(len(result[i])):
            R, C = result[i][j]
            if r == R:
                tmp = []
                for k in range(min(c, C), max(c, C)+1):
                    tmp.append((r,k))
                tmp.remove((r,c))
                result[i][j] = tmp
            else:
                tmp = []
                for k in range(min(r,R), max(r,R)+1):
                    tmp.append((k, c))
                tmp.remove((r, c))
                result[i][j] = tmp
    # print(result)
    # for i in range(len(result)):
    #     for j in range(len(i)):
            
    print(f'#{tc}')