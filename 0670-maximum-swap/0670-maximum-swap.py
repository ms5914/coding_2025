class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        
        left = -1
        right = -1

        max_so_far = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[max_so_far] > nums[i]:
                left = i
                right = max_so_far
            elif nums[i] > nums[max_so_far]:
                max_so_far = i
        if left != -1 and right != -1:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            return int("".join(nums))
        else:
            return num





        