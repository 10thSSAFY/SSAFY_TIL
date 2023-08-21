def permutation(k):
    if k == N:
        print(result_i)
        return   
    
    for i in range(N):
        if not used[i]:  # 위에서 사용하고 있지 않으면:
            used[i] = True  #i는 사용
            result_i[k] = i
            permutation(k+1)
            used[i] = False  # i사용 해제

N = 3
arr = [2, 5, 7]
result_i = [-1] * N
used = [False] * N
permutation(0)