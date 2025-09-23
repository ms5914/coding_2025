class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hm = {}
        # for i, num in enumerate(nums):
        #     if target-num in hm:
        #         return [hm[target-num], i]
        #     hm[num] = i

        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort()
        low = 0
        high = len(nums_with_index)-1

        while low<high:
            if nums_with_index[low][0]+nums_with_index[high][0] == target:
                return [nums_with_index[low][1], nums_with_index[high][1]]
            elif nums_with_index[low][0]+nums_with_index[high][0] < target:
                low+=1
            else:
                high-=1
            



        