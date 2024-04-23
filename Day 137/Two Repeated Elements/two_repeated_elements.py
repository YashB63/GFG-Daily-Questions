class Solution:
    
    def twoRepeated(self, arr , n):
        
        nums = set()
        ans = []
        for i in arr:
            if (i in nums):
                ans.append(i)
            else:
                nums.add(i)
        return ans