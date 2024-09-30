from collections import defaultdict

class Solution:

    def smallestWindow(self, s, p):
        n = len(s)
        m = len(p)
        if m>n:
            return -1
        hash_pat = defaultdict(int)
        hash_str = defaultdict(int)
        
        for i in p:
            hash_pat[i] += 1
        
        start = 0
        min_len = float("inf")
        count = 0
        start_index = -1
        
        for end in range(n):
            char = s[end]
            hash_str[char] += 1
            
            if hash_pat[char] != 0 and hash_str[char] <= hash_pat[char]:
                count += 1
            
            if count == m:
                while hash_str[s[start]] > hash_pat[s[start]] or hash_pat[s[start]] == 0:
                    if hash_str[s[start]] > hash_pat[s[start]]:
                        hash_str[s[start]] -= 1
                    start += 1
                
                window_len = end - start + 1
                if window_len < min_len:
                    min_len = window_len
                    start_index = start

        if start_index == -1:
            return "-1"
    
        return s[start_index:start_index + min_len]