class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def find_subsets(start, subset):
            result.append(list(subset))
            if start == len(nums):
                return
            for i in range(start, len(nums)):
                subset.append(nums[i])
                find_subsets(i+1, subset)
                subset.pop()
        find_subsets(0, [])
        return result
            

        