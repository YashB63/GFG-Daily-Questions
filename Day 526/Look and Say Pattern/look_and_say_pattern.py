class Solution:

    def countAndSay(self, n):
        if n == 1:
            return "1"

        curr = "1"

        for i in range(2, n + 1):
            next_str = ""
            cnt = 1

            for j in range(1, len(curr)):

                if curr[j] == curr[j - 1]:
                    cnt += 1
                    
                else:
                    next_str += str(cnt) + curr[j - 1]
                    cnt = 1

            next_str += str(cnt) + curr[-1]
            curr = next_str

        return curr