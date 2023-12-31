class Solution:
    def sumOfNaturals(self, n):
       
        sum = n*(n+1) // 2
        num = 10**9 + 7
        return sum % num