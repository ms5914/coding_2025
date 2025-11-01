class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = []

        for num in nums:
            index = bisect.bisect_left(subsequence, num)
            if index == len(subsequence):
                subsequence.append(num)
            else:
                subsequence[index] = num
        return len(subsequence)       