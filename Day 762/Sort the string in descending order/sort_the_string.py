class Solution:
    def ReverseSort(self, s):
        arr = [0] * 26
        res = []
        for char in s:
            arr[ord(char) - ord('a')] += 1

        for i in range(len(arr) - 1, -1, -1):
            while arr[i] > 0:
                arr[i] -= 1
                res.append(chr(i + ord('a')))
        
        return ''.join(res)