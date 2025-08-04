from collections import deque
from typing import List

class Solution:
    def wordLadderLength(self, startWord: str, targetWord: str,
                         wordList: List[str]) -> int:

        def ladderLengthUtility(word: str, q: deque, st: set):
            st.discard(word)

            for i in range(len(word)):
                x = word[i]

                for c in 'abcdefghijklmnopqrstuvwxyz':
                    word = word[:i] + c + word[i + 1:]

                    if word in st:
                        q.append(word)

                        st.discard(word)

                word = word[:i] + x + word[i + 1:]

        st = set(wordList)

        q = deque()

        ladderLengthUtility(startWord, q, st)

        ans = 2

        while q:
            n = len(q)

            for i in range(n):
                startWord = q.popleft()

                if startWord == targetWord:
                    return ans

                ladderLengthUtility(startWord, q, st)

            ans += 1

        return 0