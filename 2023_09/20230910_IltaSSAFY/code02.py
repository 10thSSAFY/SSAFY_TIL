import sys
sys.stdin = open('input.txt', 'r')
'''
[input]
120.0 160.0
200.0 100.0
254.0 0.0
'''

import math

def start_to_end_info(s, e):
    x = abs(s[0] - e[0])
    y = abs(s[1] - e[1])
    r = math.sqrt(x ** 2 + y ** 2)
    radian = math.atan(x/y)
    degree = math.degrees(radian)
    return r, radian, degree

def target_to_end_info(a, s, t, e):
    rx = abs(t[0] - e[0])
    ry = abs(t[1] - e[1])
    b = math.sqrt(rx ** 2 + ry ** 2)
    abx = abs(s[0] - t[0])
    aby = abs(s[1] - t[1])
    c = math.sqrt(abx ** 2 + aby ** 2)
    radian = math.acos((a**2 + b**2 - c**2)/(2*a*b))
    degree = math.degrees(radian)
    return b, radian, degree

def start_to_target_len(a, b, r2):
    d = math.sqrt((a*math.sin(r2))**2 + ((b+5.73)-(a*math.cos(r2)))**2)
    return d

def start_to_target_degree(a, b, d, d1):
    theta = d1 + math.acos((a**2 + d**2 - (b+5.73)**2)/(2*a*d))
    return theta


start = list(map(float, input().split()))  # 나의 공 위치
target = list(map(float, input().split()))  # 타겟 공 위치
end = list(map(float, input().split()))  # 홀 위치

a, r1, d1 = start_to_end_info(start, end)
# a: 내 공과 홀 까지의 거리, r1: 내 공과 홀 까지의 라디안 각 ,d1: 내 공과 홀 까지의 디그리 각
print(a, r1, d1)

b, r2, d2 = target_to_end_info(a, start, target, end)
# b: 목적구와 홀 거리, r2: 목적구와 홀까지와 내 공과 홀까지의 사이 라디안각, d2: 디그리 각
print(b, r2, d2)

d = start_to_target_len(a, b, r2)
# d: 올바른 방향으로 쳤을 때 목적구까지 닿는 순간까지의 거리
print(d)

theta = start_to_target_degree(a, b, d, d1)
# 올바른 방향으로 치기 위한 각
print(theta)