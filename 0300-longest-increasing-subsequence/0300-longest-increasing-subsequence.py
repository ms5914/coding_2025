class Solution:

    #This problem is very similar to increasing triplet subsequence where we needed two variables to set the sequence i.e first number, second number and so on. Since this is to find longest increasing subsequence we will need an array to store that. And then instead of linearly scanning where to put the next num we use binary search.
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = []

        for num in nums:
            index = bisect.bisect_left(subsequence, num)
            if index == len(subsequence):
                subsequence.append(num)
            else:
                subsequence[index] = num
        return len(subsequence)       