# 문자열 비교
import sys
sys.stdin = open('res/input_4864.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    
    result = 0
    if str1 in str2:
        result += 1

    print(f'#{tc} {result}')
