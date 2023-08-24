import sys
sys.stdin = open('res/input.txt', 'r')

binary = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
          '4':'0100', '5':'0101', '6':'0110', '7':'0111',
          '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
          'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

code = {'0001101':'0', '0011001':'1', '0010011':'2', '0111101':'3', '0100011':'4',
        '0110001':'5', '0101111':'6', '0111011':'7', '0110111':'8', '0001011':'9'}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    for l in arr:
        if l != ['0']*M:
            s1 = l
            break
    # print(s1)
    s2 = ''
    for i in s1:
        s2 += binary[i]

    for j in range(M*4-1, 0, -1):
        if s2[j] == '1':
            end = j
            break

    for k in range(0, M*4):
        if s2[k] == '1':
            start = k
            break

    # print(s2)
    k = 1
    while True:
        if 0 <= end-start < 56*k:
            break
        k += 1
    # print('k', k)
    s3 = s2[end-(56*k)+1:end+1:k]
    # print(s3)
    result = []
    for i in range(8):
        result.append(int(code[s3[i*7:(i+1)*7]]))
    # print(result)

    check = 0
    for i in range(4):
        check += (result[i*2])*3 + result[i*2+1]

    if check % 10 == 0:
        ans = sum(result)
    else:
        ans = 0

    print(f'#{tc} {ans}')