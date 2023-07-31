def my_len(lst):
    res = 0
    for i in lst:
        res += 1

    return res

def my_sum(lst):
    res = 0
    for i in lst:
        res += i

    return res

def my_min(lst):
    res = lst[0]
    idx = -1
    for i in lst:
        idx += 1
        if i < res:
            res = i
            result = i, idx
            
    return result

def my_max(lst):
    res = lst[0]
    idx = -1
    for i in lst:
        idx += 1
        if i > res:
            res = i
            result = i, idx
    return result


numbers = [10, 2, 5, 7, 12]
print(my_len(numbers))
print(my_sum(numbers))
print(my_min(numbers))
print(my_max(numbers))
