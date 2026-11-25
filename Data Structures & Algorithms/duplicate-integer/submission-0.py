class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapping = set()

        for num in nums:
            if num in mapping:
                return True
            mapping.add(num)
        
        return False