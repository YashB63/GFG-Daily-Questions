class Solution:
    def maxRepeating(self,k, arr):
        freq_Count={}
        max_freq=0
        max_num=0
        
        for num in arr:
            freq_Count[num]=freq_Count.get(num,0)+1
            
            if freq_Count[num]>max_freq:
                max_freq=freq_Count[num]
                max_num=num
            elif freq_Count[num]==max_freq and num<max_num:
                max_num=num
        return max_num