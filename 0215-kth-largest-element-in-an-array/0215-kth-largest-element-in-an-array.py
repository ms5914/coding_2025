class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        mapp = Counter(nums)
        maxim = max(mapp.keys())
        minim = min(mapp.keys())

        
        
        for i in range(maxim, minim-1,-1):
            if i in mapp:
                k-=mapp[i]
                if k<=0:
                    return i
        


    