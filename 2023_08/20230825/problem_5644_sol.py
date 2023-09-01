# 무선충전 (강사님ver)
import sys
sys.stdin = open('res/input_5644.txt')

def getPower(posA, posB):
    alst = []
    blst = []
    for i in range(A):
        x, y, C, P = BATT[i]
        if abs(posA[0]-x) + abs(posA[1]-y) <= C:
            alst.append((i, P))
        if abs(posB[0]-x) + abs(posB[1]-y) <= C:
            blst.append((i, P))

    if alst and not blst:
        return alst[0][1]
    if blst and not alst:
        return blst[0][1]
    if alst and blst:
        if alst[0] != blst[0]:
            return alst[0][1] + blst[0][1]
        nextA = nextB = 0
        P = alst[0][1]
        if len(alst) >= 2:
            nextA = alst[1][1]
        if len(blst) >= 2:
            nextB = blst[1][1]
        return max(P, P+nextA, P+nextB)
    if not alst and not blst:
        return 0


T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    moveA = list(map(int, input().split()))
    moveB = list(map(int, input().split()))

    BATT = [list(map(int, input().split())) for _ in range(A)]
    BATT.sort(reverse=True, key=lambda x:x[3])  # [[4, 4, 1, 100], [6, 3, 2, 70], [7, 10, 3, 40]]

    dx = [0, 0, 1, 0, -1]
    dy = [0, -1, 0, 1, 0]

    posA = [1, 1]
    posB = [10, 10]

    result = 0
    result += getPower(posA, posB)
    for i in range(M):
        posA[0] += dx[moveA[i]]
        posA[1] += dy[moveA[i]]
        posB[0] += dx[moveB[i]]
        posB[1] += dy[moveB[i]]
        result += getPower(posA, posB)

    print(f'#{tc} {result}')