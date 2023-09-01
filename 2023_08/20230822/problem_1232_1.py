# 사칙연산
import sys
sys.stdin = open('res/input_1232.txt', 'r')


def calc(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    elif op == '/':
        return v1 // v2


def postorder(root):
    if len(arr[root]) == 1:
        arr[root] = int(arr[root][0])
        return
    if len(arr[root]) == 3:
        postorder(int(arr[root][1]))
        l = int(arr[root][1])
        postorder(int(arr[root][2]))
        r = int(arr[root][2])
        arr[root] = calc(arr[l], arr[r], arr[root][0])
        print(arr)
  

for tc in range(1, 3):
    N = int(input())
    arr = [[] for _ in range(N+1)]
    for _ in range(N):
        lst = list(input().split())
        arr[int(lst[0])] = lst[1::]
    print(arr)
    postorder(1)
    print(f'#{tc}', arr[1])