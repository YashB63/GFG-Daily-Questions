class Solution:

    def getSubstringWithEqual012(self, Str):
        count0=0
        count1=0
        count2=0
        dic={(0,0):1}
        n=len(Str)
        count=0
        for i in range(n):
            if Str[i]=="0":
                count0+=1
            elif Str[i]=="1":
                count1+=1
            else:
                count2+=1
            diff1=count0-count1
            diff2=count0-count2
            if (diff1,diff2) in dic:
                count+=dic[(diff1,diff2)]
                dic[(diff1,diff2)]+=1
            else:
                dic[(diff1,diff2)]=1
        return count