class Solution:
    def countSpecialNumbers(self, N, arr):
        count =  0 
        dic ={}
        for i in arr :
            if i in dic :dic[i]+=1 
            else : dic[i] =1 
            
        arr.sort()
        for i in range(len(arr)):
            if dic[arr[i]] > 1 :
                count +=1 
            else : 
                for j in range(i):
                    if arr[i]%arr[j]== 0 :
                        count +=1 
                        break 
                    
        return count
