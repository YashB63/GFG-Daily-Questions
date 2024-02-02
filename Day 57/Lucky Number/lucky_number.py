class Solution:
    def isLuckyOrNot(self, N):
        
        num = str(N)
        nums = []
        luck = set()
        for i in range(len(num)):
            for j in range(i+1, len(num)+1):
                nums.append(num[i:j])
        
        for n in nums:
            prod = 1
            for digit in n:
                prod *= int(digit)
            if prod in luck:
                return 0
            luck.add(prod)
        return 1