# 백만 장자 프로젝트
import sys
sys.stdin = open('res/input_1859.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stack = list(map(int, input().split()))

    print(f'#{tc} {result}')

## 직접 구현하세요