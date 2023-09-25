def dijk(s):
    U = []
    D = [10000] * N

    D[s] = 0
    for _ in range(N):
        minV = 100000
        for i in range(N):
            if i in U:
                continue
                
            if D[i] < minV:
                minV = D[i]
                curN = i

        U.append(curN)

        for i in range(N):
            if G[curN][i] == 0:
                continue
            if D[i] > D[curN] + G[curN][i]:
                D[i] = D[curN] + G[curN][i]

        print(U)
        print(D)

N, E = map(int, input().split())
# 0이면 연결되어 있지 않다.
G = [[0] * N for _ in range(N)]
for i in range(E):
    v1, v2, w = map(int, input().split())
    G[v1][v2] = w

dijk(0)

'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''