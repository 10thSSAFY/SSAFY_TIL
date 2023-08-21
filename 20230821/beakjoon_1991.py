# 트리 순회
import sys
sys.stdin = open('res/input_beakjoon_1991.txt', 'r')

def preorder(root):
    print(root, end='')
    if arr[root][0] != '.':
        preorder(arr[root][0])
    if arr[root][1] != '.':
        preorder(arr[root][1])

def inorder(root):
    if arr[root][0] != '.':
        inorder(arr[root][0])
    print(root, end='')
    if arr[root][1] != '.':
        inorder(arr[root][1])

def postorder(root):
    if arr[root][0] != '.':
        postorder(arr[root][0])
    if arr[root][1] != '.':
        postorder(arr[root][1])
    print(root, end='')


N = int(input())
arr = dict()
for _ in range(N):
    P, L, R = input().split()
    arr[P] = [L, R]

preorder('A')
print()
inorder('A')
print()
postorder('A')
