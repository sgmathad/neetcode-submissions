class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def dfs(index, curr, result):
            if index == n:
                result.append(curr[:])
                return
            
            curr.append(nums[index])
            dfs(index + 1, curr, result)
            curr.pop()
            dfs(index + 1, curr, result)

        result = []
        dfs(0, [], result)

        return result