class Solution:
    def solve(self, arr, n):
        
        if n==1: return arr[0]
        arr.sort()
        myarr=[str(i) for i in arr]
        
        num1=''
        for i in range(0,n,2):
            num1+=myarr[i]
        num2=''
        for i in range(1,n,2):
            num2+=myarr[i]
        
        return int(num1)+int(num2)