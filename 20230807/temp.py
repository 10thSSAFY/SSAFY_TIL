lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = 5
print(lst[n])  # 6
print(lst[n:n+1])  # [6]
print(lst[n:n+2])  # [6, 7] 

print(lst[n:n-1:-1])  # [6]
print(lst[n:n-2:-1])  # [6, 5]
