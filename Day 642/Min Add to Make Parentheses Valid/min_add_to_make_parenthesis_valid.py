class Solution:
    def minParentheses(self, s: str) -> int:
        n = len(s)
        unmatchedClosing = 0
        balance = 0

        for c in s:
            if c == '(':
                balance += 1
            elif c == ')':
                balance -= 1
                if balance < 0:
                    unmatchedClosing += 1
                    balance = 0

        unmatchedOpening = 0
        balance = 0
        for c in reversed(s):
            if c == ')':
                balance += 1
            elif c == '(':
                balance -= 1
                if balance < 0:
                    unmatchedOpening += 1
                    balance = 0

        return unmatchedClosing + unmatchedOpening
