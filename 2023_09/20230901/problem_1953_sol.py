# 탈주범 검거
import sys
sys.stdin = open('res/input_1953.txt', 'r')

# 0상 1하 2좌 3우
Delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
Pipe = [[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1],
        [1, 0, 0, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]]
Opp = [1, 0, 3, 2]  # 상<->하 좌<->우


def bfs(r, c):  # 좌표r,c
    visited = [[False] * m for _ in range(n)]
    q = [(r, c, 1)]  # 큐 생성
    visited[r][c] = True

    while q:  # q에 정점이 남아있으면 front != rear
        r, c, t = q.pop(0)  # dequeue
        # 시간이 L이면 끝
        if t == l:
            break
        # 4방향에 대해
        for d in range(4):
            new_r = r + Delta[d][0]
            new_c = c + Delta[d][1]
            if 0 <= new_r < n and 0 <= new_c < m and not visited[new_r][new_c]:
                p1 = Tunnel[r][c]
                p2 = Tunnel[new_r][new_c]
                if Pipe[p1][d] and Pipe[p2][Opp[d]]:  # pipe가 연결되어 있으면
                    q.append((new_r, new_c, t + 1))
                    visited[new_r][new_c] = True
    result = 0
    for rlst in visited:
        result += rlst.count(True)
    return result


for tc in range(1, int(input()) + 1):
    n, m, r, c, l = map(int, input().split())  # n:세로 m:가로 r:세로위치 c:가로위치 l:시간
    Tunnel = [list(map(int, input().split())) for _ in range(n)]
    fin_res = bfs(r, c)
    print(f'#{tc} {fin_res}')
