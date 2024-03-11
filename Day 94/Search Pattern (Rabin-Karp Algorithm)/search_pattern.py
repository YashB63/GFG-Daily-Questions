class Solution:
    def search(self, pattern, text):
        
        naman = len(text)
        pro = len(pattern)
        a = []
        
        for i in range(naman - pro + 1):
            if text[i : i + pro] == pattern:
                a.append(i + 1)
        return a