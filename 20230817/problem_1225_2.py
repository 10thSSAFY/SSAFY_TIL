# 암호생성기
import sys
sys.stdin = open('res/input_1225.txt', 'r')

from collections import deque

def pw(que):
    while True:
        for i in range(1, 6):
            que.append(que.popleft() - i)
            if que[-1] <= 0:
                que[-1] = 0
                return que

for _ in range(10):
    tc = int(input())
    nums = list(map(int, input().split()))
    my_que = deque()
    for num in nums:
        my_que.append(num)
    result = pw(my_que)
    print(f'#{tc}', *result)
