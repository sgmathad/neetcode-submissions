class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        low = 0

        while n:
            bit = n & 1
            if bit:
                result = result | (1 << (31 - low))
            n = n >> 1
            low += 1
        
        return result