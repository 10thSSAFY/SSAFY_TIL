# 회문 2
import sys
sys.stdin = open('res/input_1216.txt', 'r')

for _ in range(10):
    tc = input()
    arr = [list(input()) for _ in range(100)]

    result = 0

    for r in range(100):
        my_str = ''
        for c in range(100):
            my_str += str(arr[r][c])
        for i in range(100):
            for j in range(100-i):
                temp = my_str[j:j+i+1]
                re_temp = temp[::-1]
                if re_temp in my_str:
                    if result < i+1:
                        result = i+1
                    break

    for c in range(100):
        my_str = ''
        for r in range(100):
            my_str += str(arr[r][c])
        for i in range(100):
            for j in range(100-i):
                temp = my_str[j:j+i+1]
                re_temp = temp[::-1]
                if re_temp in my_str:
                    if result < i+1:
                        result = i+1
                    break

    print(f'#{tc} {result}')
