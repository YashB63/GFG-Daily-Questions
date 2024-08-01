class Solution:
    def relativeSort (self,A1, N, A2, M):
        dic={}
        for i in range(M):
            dic[A2[i]]=i
        present = []
        notPresent = []
        for num in A1:
            if num in dic:
                present.append(num)
            else:
                notPresent.append(num)
        present.sort(key = lambda x:dic[x])
        notPresent.sort()
        
        return present + notPresent