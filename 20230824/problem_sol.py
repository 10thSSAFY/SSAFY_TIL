import sys
sys.stdin = open('res/input.txt', 'r')
sys.stdout = open('1.txt', 'w')

def hexToBin(hexList):
    code = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
            '4': '0100', '5': '0101', '6': '0110', '7': '0111',
            '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
            'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111' }
    return code[hexList]

PAT = [211, 221, 122, 411, 132, 231, 114, 312, 213, 112]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    hexArr = [input() for _ in range(N)]
    binArr = ['' for _ in range(N)]

    for r in range(N):
        for c in range(M):
            binArr[r] += hexToBin(hexArr[r][c])

    ans = 0
    for row in range(1, N):
        if '1' not in binArr[row]:
            continue

        col = len(binArr[0]) - 1
        while col >= 56:
            if binArr[row][col] == '1' and binArr[row-1][col] == '0':
                result = []
                for i in range(8):
                    cnt1 = 0
                    while binArr[row][col] == '1':
                        cnt1 += 1
                        col -= 1

                    cnt2 = 0
                    while binArr[row][col] == '0':
                        cnt2 += 1
                        col -= 1

                    cnt3 = 0
                    while binArr[row][col] == '1':
                        cnt3 += 1
                        col -= 1

                    cnt4 = 0
                    while binArr[row][col] == '0':
                        # cnt4 += 1
                        col -= 1
                    ratio = min(cnt1, cnt2, cnt3)
                    t = cnt3*100 + cnt2*10 + cnt1
                    t //= ratio
                    result.insert(0, PAT.index(t))
                res_sum = 0
                for i in range(4):
                    res_sum += result[i*2]*3 + result[i*2+1]
                if res_sum % 10 == 0:
                    ans += sum(result)
            else:
                col -= 1

    print(f'#{tc} {ans}')
