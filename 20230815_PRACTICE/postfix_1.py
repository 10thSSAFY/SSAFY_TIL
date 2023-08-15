infix = '(9-(4/2+1))*(5*2-2)'
postfix = ''

stack = []
icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

for i in infix:
    if i.isdigit():
        postfix += i
    elif i == ')':
        while stack and stack[-1] != '(':
            v = stack.pop()
            postfix += v
        stack.pop()  # 버림
    else:
        while stack and isp[stack[-1]] >= icp[i]:
            v = stack.pop()
            postfix += v
        stack.append(i)

while stack:
    v = stack.pop()
    postfix += v

print('postfix:', postfix)

def cal(v1, v2, op):
    if op == '+':
        return v2 + v1
    elif op == '-':
        return v2 - v1
    elif op == '*':
        return v2 * v1
    elif op == '/':
        return v2 // v1

stack = []
for i in postfix:
    if i.isdigit():
        stack.append(i)
    else:
        v2 = stack.pop()
        v1 = stack.pop()
        stack.append(cal(int(v1), int(v2), i))

result = stack.pop()

print('result:', result)