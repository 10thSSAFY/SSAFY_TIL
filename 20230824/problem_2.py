import sys
sys.stdin = open('res/input.txt', 'r')

binary = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
          '4':'0100', '5':'0101', '6':'0110', '7':'0111',
          '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
          'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

code = {'0001101':'0', '0011001':'1', '0010011':'2', '0111101':'3', '0100011':'4',
        '0110001':'5', '0101111':'6', '0111011':'7', '0110111':'8', '0001011':'9'}

T = int(input())
for tc in range(1, 6):
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    s1 = set()
    for line in arr:
        if line != '0'*M:
            s1.add(line)
    # print(s1)

    s2 = []
    for s in s1:
        line = ''
        for i in s:
            line += binary[i]
        s2.append(line)
    print(s2)

    for s in s2:
        for i in range(len(s)-1, 0, -1):
            if s[i] != '0':
                end = i
                break
        print(i)
    print(f'#{tc}')