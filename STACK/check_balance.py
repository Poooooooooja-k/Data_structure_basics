def check_balance(expression):
    stack=[]
    for char in expression:
        if char=='(':
            stack.append(char)
        elif char==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                return False
    return len(stack)==0
expression="("
res=check_balance(expression)
print(res)