class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        low = 0
        high = len(nums1)
        while low<=high:
            len_first_part = (low+high)//2
            total_len = len(nums1)+len(nums2)
            half_len = (total_len+1)//2
            len_second_path = half_len-len_first_part

            first_index = nums1[len_first_part-1] if len_first_part>0 else -float("inf")
            next_first_index = nums1[len_first_part] if len_first_part < len(nums1) else float("inf")

            second_index = nums2[len_second_path-1] if len_second_path>0 else -float("inf")
            next_second_index = nums2[len_second_path] if len_second_path < len(nums2) else float("inf")

            if first_index <= next_second_index and second_index <= next_first_index:
                if total_len%2 == 0:
                    return (max(first_index, second_index) + min(next_first_index, next_second_index))/2
                else:
                    return max(first_index, second_index)

            elif first_index>next_second_index:
                high = len_first_part-1
            else:
                low = len_first_part+1










