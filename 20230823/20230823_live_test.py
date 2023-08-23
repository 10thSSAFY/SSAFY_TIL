import sys
sys.stdin = open('input.txt', 'r')
N = int(input())    # 스위치 갯수
switch = [0] + list(map(int, input().split()))    # 스위치 상태 (0, 1)
P = int(input())    # 학생 수

female_idx = []

for _ in range(P):
    S, NUM = map(int, input().split())  # S:성별(남1, 여2), NUM:부여받은 수
    if S == 1:  # 남학생
        for i in range(NUM, N+1, NUM):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0
    else:   # 여학생
        if switch[NUM] == 0:
            switch[NUM] = 1
        else:
            switch[NUM] = 0

        for i in range(1, N):
            if 0 < NUM-i < N+1 and 0 < NUM+i < N+1 and switch[NUM-i] == switch[NUM+i]:
                female_idx.append(NUM-i)
                female_idx.append(NUM+i)
            else:
                break
        for x in female_idx:
            if switch[x] == 0:
                switch[x] = 1
            else:
                switch[x] = 0

for i in range(1, len(switch), 20):
    print(*switch[i:i+20])