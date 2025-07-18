class Solution:
    def sevenSegments(self, S: str, N: int) -> str:
        f = {
            0: 6,
            1: 2,
            2: 5,
            3: 5,
            4: 4,
            5: 5,
            6: 6,
            7: 3,
            8: 7,
            9: 5
        }

        total_segments = sum(f[int(ch)] for ch in S)

        ans = ""

        for i in range(1, N + 1):
            for j in range(10):
                remaining_segments = total_segments - f[j]
                digits_left = N - i
                
                if (remaining_segments >= 0 and 
                    2 * digits_left <= remaining_segments <= 7 * digits_left):
                    total_segments = remaining_segments
                    ans += str(j)
                    break

        return ans