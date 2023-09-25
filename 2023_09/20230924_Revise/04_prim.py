def prim(s):
    # 열결된 node의 번호를 저장
    U = []
    D = [10000] * N
    P = [-1] * N
    D[s] = 0
    for _ in range(N):
        # D의 값 중 선택되지 않은 노드 중 최선을 고른다(제일 작은 값)
        minV = 10000
        for i in range(N):
            if i in U:
                continue
            if D[i] < minV:
                minV = D[i]
                curN = i

        # curN 결정
        U.append(curN)
        
        # curN 와 연결되어 있는 노드들의 값을 최선으로 변경
        for i in range(N):
            if i in U or G[curN][i] == 0:
                continue

            if D[i] > G[curN][i]:
                D[i] = G[curN][i]
                P[i] = curN

    print(U)
    print(D)
    print(P)  # 어디 노드에서 왔는지를 기록한다.

N, E = map(int, input().split())
# 0이면 연결되어 있지 않다.
G = [[0] * N for _ in range(N)]
for i in range(E):
    v1, v2, w = map(int, input().split())
    G[v1][v2] = w
    G[v2][v1] = w

prim(0)

'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
