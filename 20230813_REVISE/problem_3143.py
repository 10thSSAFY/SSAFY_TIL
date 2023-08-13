# 가장 빠른 문자열 타이핑
import sys
sys.stdin = open('res/input_3143.txt', 'r')

def BF(t,p):
    tp = 0 # t의 초기 인덱스 위치
    pp = 0 # p의 초기 인덱스 위치
    cnt = 0
    while tp < N and pp < M:
        if t[tp] != p[pp]:
            tp = tp-pp+1
            pp = 0
        else:
            tp += 1
            pp += 1
            if pp == M:
                cnt += 1
                pp = 0
    return N-M*cnt+cnt

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    p = B # 찾는 패턴
    t = A # 전체 텍스트
    M = len(p) # 찾을 패턴의 길이
    N = len(t) # 전체 텍스트의 길이
    print(f'#{tc} {BF(t, p)}')
