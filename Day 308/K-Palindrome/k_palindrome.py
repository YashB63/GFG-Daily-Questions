def iskPalindrome(s, k):
    def lps(s, l, r, dp):
        if (l, r) in dp:
            return dp[(l, r)]
        if l > r:
            return 0
        if l == r:
            return 1 
        if s[l] == s[r]:
            return 2 + lps(s, l + 1, r - 1, dp)
        val = max(lps(s, l + 1, r, dp), lps(s, l, r - 1, dp))
        dp[(l, r)] = val 
        return val
            
    count = len(s) - lps(s, 0, len(s) - 1, {})
    return 1 if count <= k else 0