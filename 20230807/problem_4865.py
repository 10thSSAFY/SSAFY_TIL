# 글자수
import sys
sys.stdin = open('res/input_4865.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    magic_dict = dict()
    for str in str1:
        if str not in magic_dict:
            magic_dict[str] = 0

    for str in str2:
        if str in magic_dict:
            magic_dict[str] += 1
    
    result = 0
    for cnt in magic_dict.values():
        if result < cnt:
            result = cnt
    
    print(f'#{tc} {result}')
