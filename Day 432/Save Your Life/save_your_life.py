class Solution:
    def maxSum (self, w, x, b, n):
        summ = 0
        max_sum = float('-inf')
        new_ascii = dict(zip(x,b))
        ans = ''
        tmp_ans = ''
        
        for i in range(len(w)):
            if w[i] in new_ascii:
                summ += new_ascii[w[i]]
            else:
                summ += ord(w[i])
            tmp_ans += w[i]
            if summ > max_sum:
                max_sum = summ
                ans = tmp_ans
            if summ < 0:
                summ = 0
                tmp_ans = ''
        return ans