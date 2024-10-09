class Solution:
    def findMajority(self, nums):
        cnt1, cnt2 = 0,0
        el1, el2 = float('-inf'), float('-inf')
        min_votes = (len(nums)//3)+1
        
        for num in nums:
            if cnt1 == 0 and el2 != num:
                cnt1+=1
                el1 = num
            elif cnt2 == 0 and el1 != num:
                cnt2+=1
                el2 = num
            
            elif num == el1: cnt1+=1
            
            elif num == el2: cnt2+=1
            
            else: cnt1-=1 ; cnt2-=1
        
        cnt1,cnt2 = 0,0
        for num in nums:
            if num == el1 : cnt1+=1
            if num == el2 : cnt2+=1
        res = []
        if cnt1 >= min_votes: res.append(el1)
        if cnt2 >= min_votes: res.append(el2)
        if not res: res.append(-1)
        return res