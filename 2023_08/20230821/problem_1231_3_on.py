# [S/W 문제해결 기본] 9일차 - 중위순회
import sys
sys.stdin = open('res/input_1231.txt', 'r')

def inorder(root):
    global ans
    if root <= N:
        inorder(root*2)
        ans += lst[root]
        inorder(root*2 + 1)

T = 10
for t in range(1, T+1):
    N = int(input())
    lst = [0]*(N+1)
    for i in range(1, N+1):
        tlst = input().split()
        lst[i] = tlst[1]
    ans = ''
    inorder(1)

    print(f'#{t} {ans}')
