class Solution:
    def powerSetUtil(self, s, index, curr, ans):
        if index == len(s):
            ans.append(curr)
            return
        
        self.powerSetUtil(s, index + 1, curr, ans)
        self.powerSetUtil(s, index + 1, curr + s[index], ans)

    def powerSet(self, s):
        ans = []
        self.powerSetUtil(s, 0, "", ans)
        return ans