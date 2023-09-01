# [S/W 문제해결 기본] 9일차 - 중위순회
import sys
sys.stdin = open('res/input_1231.txt', 'r')

def inorder(root):
    global value
    if root > N:
        return
    inorder(root * 2)
    A_i[root-1] = value-1
    value += 1
    inorder(root * 2 + 1)


for tc in range(1, 11):
    N = int(input())
    A = []
    for _ in range(N):
        arr = list(input().split())
        A.append(arr[1])
    A_i = [0] * N
    value = 1
    inorder(1)
    result = [0]*N
    for i in range(N):
        result[A_i[i]] = A[i]
    print(f'#{tc}', ''.join(result))
