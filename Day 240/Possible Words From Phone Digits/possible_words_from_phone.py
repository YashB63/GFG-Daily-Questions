class Solution:
    
    values =["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    
    def helper(self,index,arr,N,temp,result):
        if index == N:
            result.append("".join(temp))
            return
            
        for i in range(len(self.values[arr[index]])):
            temp.append(self.values[arr[index]][i])
            self.helper(index+1,arr,N,temp,result)
            temp.pop()
            
    def possibleWords(self,a,N):
        result=[]
        self.helper(0,a,N,[],result)
        return result