class Solution:
	def search(self,pat, txt):
        k = len(pat)
        i = 0
        j = 0
        dict = {}
        for ele in pat:
            if ele in dict:
                dict[ele] += 1
            else:
                dict[ele] = 1
                
        
        count = len(dict)
        ans = 0
        
        while j < len(txt):
            if txt[j] in dict:
                dict[txt[j]] -= 1
                if dict[txt[j]] == 0:
                    count -= 1
        
            if j-i+1 < k:
                j += 1
            else:
                if count == 0:
                    ans += 1
                
                if txt[i] in dict:
                    dict[txt[i]] += 1
                    if dict[txt[i]] == 1:
                        count += 1
                i += 1
                j += 1
        return ans