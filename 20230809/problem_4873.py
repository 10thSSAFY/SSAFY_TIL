# 반복문자 지우기
import sys
sys.stdin = open('res/input_4873.txt', 'r')

def del_double(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack)


T = int(input())
for t in range(1, T+1):
    s = input().strip()
    result = del_double(s)
    print(f"#{t} {result}")
