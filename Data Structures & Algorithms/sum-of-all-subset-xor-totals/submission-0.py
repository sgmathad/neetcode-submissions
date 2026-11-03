class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(index, curr, result):
            if index == len(nums):
                result[0] += curr
                return
            
            curr ^= nums[index]
            dfs(index + 1, curr, result)
            curr ^= nums[index]
            dfs(index + 1, curr, result)
        
        result = [0]
        dfs(0, 0, result)
        return result[0]