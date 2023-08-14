# Forth
import sys
sys.stdin = open('res/input_4874.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    lst = list(input().split())
    stack = []
    for i in lst:
        if i in '+-*/':
            if i == '+':
                if len(stack) >= 2:
                    stack.append(stack.pop() + stack.pop())
                else:
                    result = 'error'
                    break
            elif i == '-':
                if len(stack) >= 2:
                    stack.append(-stack.pop() + stack.pop())
                else:
                    result = 'error'
                    break
            elif i == '*':
                if len(stack) >= 2:
                    stack.append(stack.pop() * stack.pop())
                else:
                    result = 'error'
                    break
            elif i == '/':
                if len(stack) >= 2:
                    o2 = stack.pop()
                    o1 = stack.pop()
                    stack.append(o1 // o2)
                else:
                    result = 'error'
                    break
        elif i == '.':
            if len(stack) == 1:
                result = stack.pop()
                break
            else:
                result = 'error'
                break
        else:
            stack.append(int(i))
            
    print(f'#{tc} {result}')