class Solution:
    def klengthpref(self,arr,n,k,s):
        if k>len(s):
            return 0
        else:
            str1=s[:k]
            count=0
            for i in range(n):
                if str1==arr[i][:k]:
                    count=count+1
        return count