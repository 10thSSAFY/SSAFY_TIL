def partial(k):
    if k == N:
        print(result_i)
        for i in range(N):
            if result_i[i]:
                print(arr[i], end = ' ')
        print()
        return
    
    result_i[k] = 0
    partial(k+1)
    
    result_i[k] = 1
    partial(k+1)
    
N = 3
arr = [2, 5, 7]
result_i = [-1] * N

partial(0)