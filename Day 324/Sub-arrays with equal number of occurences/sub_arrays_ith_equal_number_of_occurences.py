class Solution:
    def sameOccurrence(self, arr, x, y):
        count=ans=0
        hmap={}
        hmap[0]=1
        for i in arr:
            if i==x:
                count+=1
            if i==y:
                count-=1
            if count in hmap.keys():
                ans+=hmap[count]
                hmap[count]=hmap[count]+1
            else:
                hmap[count]=1
        return ans