# [S/W 문제해결 기본] 9일차 - 중위순회
import sys
sys.stdin = open('res/input_1231.txt', 'r')
## 강사님 조언
def inorder(root):
    global result
    if len(TREE[root]) >= 2:
        inorder(int(TREE[root][1]))
    result += TREE[root][0]
    if len(TREE[root]) >= 3:
        inorder(int(TREE[root][2]))


for tc in range(1, 11):
    N = int(input())
    TREE = [[] for _ in range(N+1)]
    for _ in range(N):
        s = input().split()
        # print(s)
        no = int(s[0])
        TREE[no] = s[1::]
    # print(TREE)
    result = ''
    inorder(1)
    print(f'#{tc} {result}')
