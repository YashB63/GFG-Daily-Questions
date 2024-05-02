class Solution:
    def isProduct(self, arr, n, x):
        
        s=set()
        for i in arr:
            if i==0:
                if x==0:
                    
                    return True
                else:
                    continue
            else:
                
                    if (x/i) in s:
                        return True
                    else:
                        s.add(i)
        return False