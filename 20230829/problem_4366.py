# 정식이의 은행업무
import sys
sys.stdin = open('res/input_4366.txt', 'r')

def ssafy():
    for r2 in res2:
        for r3 in res3:
            if r2 - r3 == 0:
                return r2

T = int(input())
for tc in range(1, T + 1):
    num2 = list(input().strip())
    num3 = list(input().strip())
    lst2 = []
    lst3 = []
    for i in range(len(num2)):
        tmp = [-1] * len(num2)
        if num2[i] == '0':
            tmp[i] = '1'
        else:
            tmp[i] = '0'
        for j in range(len(num2)):
            if tmp[j] == -1:
                tmp[j] = num2[j]
        tmp_res = ''.join(tmp)
        lst2.append(tmp_res)

    for i in range(len(num3)):
        tmp = [-1] * len(num3)
        tmp[i] = str((int(num3[i]) + 1) % 3)
        for j in range(len(num3)):
            if tmp[j] == -1:
                tmp[j] = num3[j]
        tmp_res = ''.join(tmp)
        lst3.append(tmp_res)

    for i in range(len(num3)):
        tmp = [-1] * len(num3)
        tmp[i] = str((int(num3[i]) + 2) % 3)
        for j in range(len(num3)):
            if tmp[j] == -1:
                tmp[j] = num3[j]
        tmp_res = ''.join(tmp)
        lst3.append(tmp_res)

    # print(lst2)  # ['0010', '1110', '1000', '1011']
    # print(lst3)  # ['012', '222', '210', '112', '202', '211']

    res2 = []
    res3 = []
    for l2 in lst2:
        curr_sum = 0
        tmp = 1
        for i in range(len(l2)):
            if l2[-1 - i] == '1':
                curr_sum += tmp
            tmp *= 2
        res2.append(curr_sum)
    # print(res2)  # [2, 14, 8, 11]

    for l3 in lst3:
        curr_sum = 0
        tmp = 1
        for i in range(len(l3)):
            if l3[-1 - i] == '1':
                curr_sum += tmp
            elif l3[-1 - i] == '2':
                curr_sum += tmp*2
            tmp *= 3
        res3.append(curr_sum)
    # print(res3)  # [5, 26, 21, 14, 20, 22]
    
    result = ssafy()
    print(f'#{tc} {result}')
