def start_end_len(s, e):
    x = abs(s[0] - e[0])
    y = abs(s[1] - e[1])
    r = math.sqrt(x**2 + y**2)
    radian = math.atan(x/y)
    degree = math.degrees(radian)
    return (r, radian, degree)

def target_ent_len(t, e):
    x = abs(t[0] - e[0])
    y = abs(t[1] - e[1])
    r = math.acos(()/())
    radian = math.atan(x/y)


def to_target_len(a, b, r2):
    res = math.sqrt((a * math.sin(r2)) ** 2 + ((b + 5.73) - (a * math.cos(r2))) ** 2)
    return res

import math

# 두 점의 좌표
start = (120.0, 60.0)  # 내 공
end = (254.0, 0.0)  # 홀의 위치
target = (200.0, 100.0)  # 타겟 공의 위치

a, r1, d1 = start_end_len(start, end)  # a: 내 공과 홀 거리, d1: 내 공이 홀을 향하는 각
print(a, r1, d1)
b, r2, d2 = target_end_len(target, end)  # b: 타겟 공과 홀 거리, d2: 타겟 공이 홀을 향하는 각과
print(b, r2, d2)
d = to_target_len(a, b, r2)  # 내가 쳐야 할 방향으로 쳤을 때 목적구에 닿는 순간 까지의 거리
print(d)

c, r3, d3 = to_target_degree(a, b, d)