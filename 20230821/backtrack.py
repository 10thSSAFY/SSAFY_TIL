# 백트래킹 가지치기
def print_result():
    for i in range(N):
        if result_i[i]:
            print(arr[i], end=' ')
    print()

def partial(k, curSum):
    if curSum > 10:
        return  # 백트래킹
    if k == N:
        # sumV = 0
        # for i in range(N):
            # if result_i[i]:
                # sumV += arr[i]
        if curSum == 10:
            print_result()
        return
    
    result_i[k] = 0
    partial(k+1, curSum)
    
    result_i[k] = 1
    partial(k+1, curSum+arr[k])

N = 10
arr = [i for i in range(1, 11)]
result_i = [-1] * N
partial(0, 0)