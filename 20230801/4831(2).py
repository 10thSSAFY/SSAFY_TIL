import sys
sys.stdin = open('4831.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    a, b, c = map(int, input().split())
    d = list(map(int, input().split()))
    d.append(b)
    count = 0
    where = 0
    for i in range(c):
        if d[i + 1] > a + where:
            count += 1
            where = d[i]
    d = [0] + d
    for i in range(1, len(d)):
        if d[i] - d[i - 1] > a:
            count = 0
    print(f"#{test_case} {count}")
