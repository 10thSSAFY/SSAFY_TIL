def fix(s):
    stack = []
    postfix = ''
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    for i in s:
        if i.isdigit():
            postfix += i
        elif i == ')':
            while stack and stack[-1] != '(': # 스택의 탑이 '(' 아닐 때까지 postifx에 저장
                v = stack.pop()
                postfix += v
            stack.pop() # '(' 버림
        else: # infix == '(', '+', '-', '*', '/'
            while stack and isp[stack[-1]] >= icp[i]:
                v = stack.pop()
                postfix += v
            stack.append(i)
    
    while stack:
        v = stack.pop()
        postfix += v
    return postfix

def cal(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v2 - v1
    elif op == '*':
        return v1 * v2
    elif op == '/':
        return v2 // v1

def decimal(s):
    stack = []
    for i in s:
        if i.isdigit():
            stack.append(i)
        else:
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(cal(int(v1), int(v2), i))
    return stack.pop()        


infix = '(9-(4/2+1))*(5*2-2)'
print('infix:', infix)

postfix = fix(infix)
print('postfix:', postfix)

result = decimal(postfix)
print('result:', result)
