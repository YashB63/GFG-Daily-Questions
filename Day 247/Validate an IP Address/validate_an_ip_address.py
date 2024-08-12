class Solution:
    def isValid(self, str):
        
        lst=str.split('.')
        
        for i in lst:
            if len(i)<1:
                lst.remove(i)
                
        if len(lst)==4:
            flag=0
            for i in lst:
                if 0<=int(i)<=255:
                    if len(i)>1 and i[0]=='0':
                        flag=0
                    else:
                        flag+=1
            if flag==4:
                return True
            return False
        return False