# 사칙연산  # 
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
    if arr[root][0].isdecimal():
        return int(arr[root][0])
    else:
        vl = postorder(int(arr[root][1]))
        vr = postorder(int(arr[root][2]))
        return calc(vl, vr, arr[root][0])


for tc in range(1, 11):
    N = int(input())
    arr = [[] for _ in range(N+1)]
    for _ in range(N):
        lst = list(input().split())
        arr[int(lst[0])] = lst[1::]

    result = postorder(1)
    print(f'#{tc} {result}')
