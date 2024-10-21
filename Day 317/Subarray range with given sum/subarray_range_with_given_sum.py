class Solution:
    
    def subArraySum(self,arr, tar):
        sum = {0:1}
        cumsum  = 0
        count = 0
        for number in arr:
            cumsum += number
            if sum.get(cumsum-tar)!=None:
                count += sum.get(cumsum-number)
            if sum.get(cumsum):
                sum[cumsum] += 1
            else:
                sum[cumsum] = 1
        return count