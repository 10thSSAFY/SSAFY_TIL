# 숫자 배열 회전
import sys
sys.stdin = open('res/input_1961.txt', 'r')

def rotate(array):
    n = len(array)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = array[i][j]
    return rotated

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    arr_90 = rotate(arr)
    arr_180 = rotate(arr_90)
    arr_270 = rotate(arr_180)
    
    print(f"#{tc}")
    for i in range(N):
        result_90 = ''.join(map(str, arr_90[i]))
        result_180 = ''.join(map(str, arr_180[i]))
        result_270 = ''.join(map(str, arr_270[i]))
        print(result_90, result_180, result_270)
