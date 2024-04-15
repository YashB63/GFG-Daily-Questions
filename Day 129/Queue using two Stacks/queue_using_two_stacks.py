def Push(x,stack1,stack2):
    
    stack1.append(x)

def Pop(stack1,stack2):
   
    if stack1 == []: 
        return -1
    else : 
        return stack1.pop(0)