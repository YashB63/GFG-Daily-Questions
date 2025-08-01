from typing import List

class Solution:
    def findRollOut(self, s: str, roll: List[int]) -> str:
        rollSize = len(roll)
        strSize = len(s)
        alphabetCount = 26

        rollOutPrefix = [0] * (strSize + 1)

        for i in range(rollSize):
            rollOutPrefix[0] += 1
            if roll[i] < strSize:
                rollOutPrefix[roll[i]] -= 1

        for i in range(1, strSize):
            rollOutPrefix[i] += rollOutPrefix[i - 1]

        result = []
        for i in range(strSize):
            rollValue = rollOutPrefix[i] % alphabetCount

            currentCharPos = ord(s[i]) - ord('a')

            result.append(
                chr(ord('a') + (currentCharPos + rollValue) % alphabetCount))

        return ''.join(result)