from collections import defaultdict

class Solution:
	def topKFrequent(self, arr, k):
        hm = defaultdict(int)
        for i in arr:
            hm[i] += 1
        
        sorted_dict = sorted(hm.items(), key=lambda x: (-x[1], -x[0]))
        
        ans = []
        for i in range(k):
            ans.append(sorted_dict[i][0])
        
        return ans