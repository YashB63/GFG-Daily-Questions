class Solution:
    def allPossibleSubsequences(ob, S):
        def find(index, output, S, ans, l, vowel):
            if index == l:
                if output and output[0] in vowel and output[-1] not in vowel:
                    ans.add(output)
                return
            
            find(index + 1, output + S[index], S, ans, l, vowel)
            find(index + 1, output, S, ans, l, vowel)

        vowel = {'a', 'e', 'i', 'o', 'u'}
        ans = set()
        l = len(S)
        find(0, "", S, ans, l, vowel)
        return sorted(ans)