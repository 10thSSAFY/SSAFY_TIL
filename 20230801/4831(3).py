T = int(input())
for i in range(1,T+1):
    K,N,M = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.append(N)
    lst.append(0)
    lst = sorted(lst)
    if lst[1] > K :
        print(f'#{i}',0)
    else:
        cnt = 0
        lst_ =[0]
        for k in lst_:
            if k == M+1:
                break
            elif k > 0 and k == lst_[len(lst_)-2]:
                print(f'#{i}',0)
                break
            else:
                for j in range(len(lst)-1,-1,-1):
                    if lst[k]+K >= lst[j]:
                        cnt += 1
                        lst_.append(j)
                        break
        if lst_[-1] == M+1:
            print(f'#{i}',cnt-1)
