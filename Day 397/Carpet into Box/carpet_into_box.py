class Solution:
    
    def solve(self, carpet_len, carpet_breath, box_len, box_breath):
        moves = 0

        while carpet_len > box_len:
            carpet_len //= 2
            moves += 1

        while carpet_breath > box_breath:
            carpet_breath //= 2
            moves += 1

        return moves
        
    def carpetBox(self, carpet_len, carpet_breath, box_len, box_breath):
        reduced_len    = self.solve(carpet_len, carpet_breath, box_len, box_breath)
        reduced_breath = self.solve(carpet_breath, carpet_len, box_len, box_breath)

        return min(
            reduced_len,
            reduced_breath
        )