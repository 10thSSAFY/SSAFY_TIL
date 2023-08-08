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
            my_str += arr[r][c]
        reverse_str = my_str[::-1]
        
        ap = 0
        bp = 0
        result = 0
        cnt = 0
        while ap != 0 or bp != 99 :
            if bp == 100:
                bp = 101-ap
                ap = 0
                cnt = 0
                continue
            elif my_str[ap] == reverse_str[bp]:
                cnt +=1
            elif my_str[ap] != reverse_str[bp]:
                if result < cnt:
                    result = cnt
                cnt = 0
            ap += 1
            bp += 1

    for c in range(100):
        my_str = ''
        for r in range(100):
            my_str += arr[r][c]
        reverse_str = my_str[::-1]
        
        ap = 0
        bp = 0
        cnt = 0
        while ap != 0 or bp != 99 :
            if bp == 100:
                bp = 101-ap
                ap = 0
                cnt = 0
                continue
            elif my_str[ap] == reverse_str[bp]:
                cnt +=1
            elif my_str[ap] != reverse_str[bp]:
                if result < cnt:
                    result = cnt
                cnt = 0
            ap += 1
            bp += 1

    print(f'#{tc} {result}')
