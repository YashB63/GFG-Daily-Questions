class Solution:
    def countSort(self, s):
        freq = [0] * 256

        for char in s:
            freq[ord(char)] += 1

        arr = ""
        for i in range(256):
            for j in range(freq[i]):
                arr += chr(i)

        return arr