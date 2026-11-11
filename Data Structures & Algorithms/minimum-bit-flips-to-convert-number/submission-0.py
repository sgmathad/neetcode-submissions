class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        result = 0
        while xor:
            result += (xor & 1)
            xor = xor >>1
        
        return result
