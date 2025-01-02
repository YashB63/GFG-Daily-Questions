class Solution:
	def twoSum(self, arr, target):
        ch={}
        for i in arr:
            if target-i in ch:
                return True
            ch[i]=True
        return False