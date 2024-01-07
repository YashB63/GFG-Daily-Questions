class Solution:
    
    def ispar(self,x):
        
        a = []
        
        def match(z,w):
            if(z == '(' and w == ')'):
                return 1
            elif(z == '{' and w == '}'):
                return 1
            elif(z == '[' and w == ']'):
                return 1
            else:
                return 0
                
        for i in x:
            if i == '[' or i == '{' or i == '(':
                a.append(i)
            
            elif i == ']' or i == '}' or i == ')':
                if len(a) == 0:
                    return False
                    
                elif match(a[-1], i):
                    a.pop()
                
                else:
                    return False
                    
        if len(a) == 0:
            return True
        else:
            return False