class Solution:
    def longestSubstrDistinctChars(self, S):
        count=0
        a=[]
        count1=0
        for i in S:
            if i not in a:
                a.append(i)
                count+=1
            else:
                if count > count1:
                    count1 = count
                a = a[a.index(i) + 1:]  
                a.append(i)
                count = len(a)
        return max(count, count1)