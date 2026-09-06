class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = ord(s[0])
        total = 0

        for j in range(1, len(s)):
            curr = ord(s[j])
            total += abs(curr - prev)
            prev = curr
        return total