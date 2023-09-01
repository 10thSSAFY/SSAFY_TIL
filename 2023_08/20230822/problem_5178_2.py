# 5178 노드의 합  # 강사님의 조언
import sys
sys.stdin = open('res/input_5178.txt', 'r')

def postOrder(root):
    if root > N:
        return 0
    
    if TREE[root]:
        return TREE[root]

    vl = postOrder(root*2)
    vr = postOrder(root*2 + 1)
    TREE[root] = vl + vr
    return TREE[root]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    TREE = [0] * (N+1)
    for i in range(M):
        nodeNo, value = map(int, input().split())
        TREE[nodeNo] = value

    postOrder(1)
    print(f'#{tc} {TREE[1]}')