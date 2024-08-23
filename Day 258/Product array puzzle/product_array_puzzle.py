class Solution:
    def productExceptSelf(self, nums):
        zero_count=nums.count(0)
        n=len(nums)
        if zero_count>1:
            return [0]*n
        else:
            if zero_count==1:
                product=1
                for i in range(n):
                    if nums[i]!=0:
                        product*=nums[i]
                    else:
                        zero_index=i
                nums=[0]*n
                nums[zero_index]=product
                return nums
            else:
                product=1
                for i in nums:
                    product*=i
                for i in range(n):
                    nums[i]=product//nums[i]
                return nums