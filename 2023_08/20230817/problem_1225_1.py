# 암호생성기
import sys
sys.stdin = open('res/input_1225.txt', 'r')

def pw(lst):
    while True:
        for i in range(1, 6):
            lst.append(lst.pop(0) - i)
            if lst[-1] <= 0:
                lst[-1] = 0
                return lst

for _ in range(10):
    tc = int(input())
    nums = list(map(int, input().split()))
    result = pw(nums)
    print(f'#{tc}', *result)
