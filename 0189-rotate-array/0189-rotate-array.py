class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # #Remember this : Don't forget this 
        # k%=len(nums)
        # def reverse_array(nums, i, j):
        #     while i<j:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i+=1
        #         j-=1

        # nums.reverse() #Full reverse to get the last k items first
        # reverse_array(nums, 0,k-1) # Reverse those k items to get them in order
        # reverse_array(nums, k, len(nums)-1) # Reverse the others to undo the previous reverse


        count = 0
        n = len(nums)
        k%=n

        start = 0
        while count<n:
            current = start
            curr_num = nums[current]
            while True:
                next_index = (current+k)%n
                next_num = nums[next_index]
                nums[next_index], curr_num = curr_num, next_num
                current = next_index
                count+=1

                if current == start:
                    start+=1
                    break
        return nums
        


        