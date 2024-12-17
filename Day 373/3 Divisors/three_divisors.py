import math

class Solution:
	def threeDivisors(self, query, q):
        arr = []
        for i in query:
            j = 2
            count = 0
            while(j <= i):
                flag = 1
                k = 2
                while(k<=math.sqrt(j)):
                    if(j%k == 0):
                        flag = 0
                        break
                    k+=1
                    
                if(j**2 > i):
                    break
                if(flag):
                    count+=1
                j+=1
                    
            arr.append(count)
                
        return(arr)
