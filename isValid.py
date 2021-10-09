def isValid(s: str) -> bool:
    if len(s)%2!=0:return False
    
    stack = []
    cuenta = 0
    
    for i in s:
        if (i=='(' or i=='{' or i=='['):
            stack.append(i)
            cuenta+=1
        elif(i == ')' and cuenta>0 and stack[cuenta-1]=='('):
            stack.pop()
            cuenta-=1
        elif(i == ']' and cuenta>0 and stack[cuenta-1]=='['):
            stack.pop()
            cuenta-=1
        elif(i == '}' and cuenta>0 and stack[cuenta-1]=='{'):
            stack.pop()
            cuenta-=1
        else:
            return False
    return True if cuenta == 0 else False

s = "([}}])"
print(isValid(s))