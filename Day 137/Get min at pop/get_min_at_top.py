def _push(a,n):

    stack=[]
    stack.append(a[0])
    for i in range(1,n):
        stack.append(min(stack[-1],a[i]))
    return stack

def _getMinAtPop(stack):
    
    if not stack:
        return None
    while(stack):
        print(stack[-1],end=" ")
        stack.pop()