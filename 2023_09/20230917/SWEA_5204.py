import sys
sys.stdin = open('res/input_SWEA_5204.txt', 'r')

def merge(arr):
    global cnt
    if len(arr) == 1:
        return arr
    left = merge(arr[0:(len(arr))//2])
    right = merge(arr[(len(arr))//2:])
    if left[-1] > right[-1]:
        cnt += 1
    l, r = 0, 0
    res = []
    while l < len(left) or r < len(right):
        if l == len(left):
            res.append(right[r])
            r += 1
        elif r == len(right):
            res.append(left[l])
            l += 1
        elif left[l] > right[r]:
            res.append(right[r])
            r += 1
        elif left[l] <= right[r]:
            res.append(left[l])
            l += 1
    return res

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    res_lst = merge(arr)
    print(f'#{tc}', res_lst[N//2], cnt)