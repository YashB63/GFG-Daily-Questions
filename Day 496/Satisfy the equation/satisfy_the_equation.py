from collections import defaultdict

class Solution:
    def satisfyEqn(self, a, N):
        map = defaultdict(list)
        ans = 0
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                s = (a[i]+a[j])
                if s in map:
                    if map[s][0]!=i and map[s][1]!=j and map[s][0]!=j and map[s][1]!=i:
                        temp = map[s][:2]+[i,j]
                        if not ans or ans>temp:
                            while map[s]:
                                map[s].pop()
                            map[s].extend(temp)
                            ans = map[s]
                else:
                    map[s].extend([i,j])
        return ([-1,-1,-1,-1]) if not ans else ans