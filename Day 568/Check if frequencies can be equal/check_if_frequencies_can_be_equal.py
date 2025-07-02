class Solution:
    def sameFreq(self, s: str) -> bool:
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        freqCount = {}

        for f in freq:
            if f > 0:
                freqCount[f] = freqCount.get(f, 0) + 1

        if len(freqCount) == 1:
            return True  

        if len(freqCount) == 2:
            items = list(freqCount.items())
            freq1, count1 = items[0]
            freq2, count2 = items[1]

            if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
                return True

            if abs(freq1 - freq2) == 1 and ((count1 == 1 and freq1 > freq2) or
                                            (count2 == 1 and freq2 > freq1)):
                return True

        return False