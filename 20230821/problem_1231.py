# [S/W 문제해결 기본] 9일차 - 중위순회
import sys
sys.stdin = open('res/input_1231.txt', 'r')

def inorder(root):
    global value
    if root > N:
        return
    inorder(root * 2)
    newarr[root] = value
    value += 1
    inorder(root * 2 + 1)


for tc in range(1, 11):
    N = int(input())
    newlst = []
    for _ in range(N):
        arr = list(input().split())
        newlst.append(arr[1])
    newarr = [0] * (N+1)
    value = 1
    inorder(1)
    for i in range(1, N):
        print(newlst[i], end= ' ')
    print(f'#{tc}')

'''
## 강사님의 조언
N = int(input())
TREE = [[] for _ in range(N+1)]

for _ in range(N):
    s = input().split()
    # print(s)
    no = int(s[0])
    TREE[no] = s[1::]

print(TREE)
'''
