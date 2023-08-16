# 배열 최소 합
import sys
sys.stdin = open('res/input_4881.txt', 'r')

def backtrack(row, curr_sum):
    global min_sum
    if curr_sum > min_sum:
        return

    if row == n:
        if min_sum > curr_sum:
            min_sum = curr_sum
        return

    for i in range(n):
        if not used[i]:
            used[i] = True
            backtrack(row+1, curr_sum + nums[row][i])
            used[i] = False


t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]

    min_sum = 0
    for num in nums:
        min_sum += max(num)

    used = [False] * n
    backtrack(0, 0)
    print(f"#{test_case} {min_sum}")
