class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        maxFavor = float('inf')
        result = []
        nums = cookies
        n = len(nums)

        def find_split(index, subset_sums, subsets, nums):
            nonlocal maxFavor, n, result
            if index == n:
                if max(subset_sums) < maxFavor:
                    maxFavor = max(subset_sums)
                    result = [list(subsets[i]) for i in range(len(subsets))]
                return
            if max(subset_sums) >= maxFavor:
                return
            for i in range(k):
                subsets[i].append(nums[index])
                subset_sums[i] += nums[index]
                if max(subset_sums) < maxFavor:
                    find_split(index + 1, subset_sums, subsets, nums)
                subsets[i].pop()
                subset_sums[i] -= nums[index]
        find_split(0, [0] * k, [[] for _ in range(k)], nums)
        return maxFavor
        
        