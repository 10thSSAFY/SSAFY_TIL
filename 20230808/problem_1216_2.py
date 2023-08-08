# 회문 2
import sys
sys.stdin = open('res/input_1216.txt', 'r')

for _ in range(10):
    tc = input()
    arr = [input() for _ in range(100)]
    result = 0
    for line in arr:
        for i in range(100):
            for j in range(100-i):
                my_str = line[j:j+i+1]
                re_my_str = my_str[::-1]
                if re_my_str in line:
                    if result < i+1:
                        result = i+1
    
    for r in range(100):
        str = ''


    # print(arr[0][0:1])
    # print(arr[0][99:100])
    # print(arr[0][0:100])



    print(f'#{tc} {result}')
