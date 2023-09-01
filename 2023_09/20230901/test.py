T = int(input())
cnt = 0
while T != 1:
    if T % 3 == 0:
        T = T // 3
        cnt += 1
    elif (T-1) % 3 == 0:
        T = (T-1) // 3
        cnt += 2
    elif T % 2 == 0:
        T = T // 2
        cnt + 1
    elif (T-2) % 3 == 0:
        T = (T-2) // 3
        cnt += 3
    elif (T-1) % 2 == 0:
        T = (T-1) // 2
        cnt += 2
    
print(cnt)