import sys
sys.stdin = open('res/input_Contact.txt', 'r')

def BFS(start):
    visited = [False] * 101
    visited[start] = True
    queue = [start]
    while queue:
        connection = []
        for _ in range(len(queue)):
            v = queue.pop(0)
            connection.append(v)
            for w in graph[v]:
                if not visited[w]:
                    queue.append(w)
                    visited[w] = True
    return connection

for tc in range(1, 11):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        graph[lst[i]].append(lst[i+1])
    connectlst = BFS(S)
    result = max(connectlst)
    print(f'#{tc} {result}')
