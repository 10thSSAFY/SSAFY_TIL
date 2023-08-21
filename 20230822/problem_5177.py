# 5177 이진 힙
import sys
sys.stdin = open('res/input_5177.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    heap = [0]

    for num in nums:
        heap.append(num)
        index = len(heap) - 1

        while index > 1 and heap[index] < heap[index // 2]:
            heap[index], heap[index // 2] = heap[index // 2], heap[index]
            index //= 2

    last_index = len(heap) - 1
    ancestors_sum = 0
    while last_index > 1:
        last_index //= 2
        ancestors_sum += heap[last_index]

    print(f"#{t} {ancestors_sum}")
