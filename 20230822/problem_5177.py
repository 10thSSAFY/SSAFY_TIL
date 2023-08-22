# 5177 이진 힙
import sys
sys.stdin = open('res/input_5177.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    HEAP = [0]
    for num in nums:
        HEAP.append(num)
        last = len(HEAP) - 1
        c = last
        while c > 1 and HEAP[c] < HEAP[c//2]:
            HEAP[c], HEAP[c//2] = HEAP[c//2], HEAP[c]
            c //= 2

    c = N
    result = 0
    while c > 1:
        result += HEAP[c//2]
        c //= 2

    print(f"#{t} {result}")
