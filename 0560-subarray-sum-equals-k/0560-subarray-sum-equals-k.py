class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        curr_sum = 0
        count = 0
        hm[0] = 1
        for num in nums:
            curr_sum+=num
            if curr_sum-k in hm:
                count+=hm[curr_sum-k]
            hm[curr_sum]+=1
        return count
        

            

