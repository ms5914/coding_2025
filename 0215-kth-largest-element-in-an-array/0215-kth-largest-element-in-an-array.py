class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        def partition(nums, p, r):
            index = random.randint(p, r)
            pivot_ele = nums[index]
            nums[r], nums[index] = nums[index], nums[r]
            less_ind = p
            for ind in range(p, r):
                on_left = random.randint(0, 1) == 1
                if nums[ind] < pivot_ele:
                    nums[ind], nums[less_ind] = nums[less_ind], nums[ind]
                    less_ind+=1
                elif nums[ind] == pivot_ele and on_left:
                    nums[ind], nums[less_ind] = nums[less_ind], nums[ind]
                    less_ind+=1
            nums[less_ind], nums[r] = nums[r], nums[less_ind]
            return less_ind
                
        
        def find_k_largest(nums, p, r):
            if p>r:
                return
            pivot = partition(nums, p, r)
            if pivot == n-k:
                return nums[n-k]
            
            elif pivot< n-k:
                return find_k_largest(nums, pivot+1, r)
            else:
                return find_k_largest(nums, p, pivot-1)
            
        
        
        return find_k_largest(nums, 0, n-1)
    
    
    
    
#     class Solution {
#     int quickSelect(int l, int r, int k, vector<int>& nums) {
#         int randomIdx = rand() % (r - l + 1) + l;
#         swap(nums[randomIdx], nums[r]);
#         int p = l;
#         for(int i = l; i < r; ++i) {
#             int couldBeSame = rand() % 2;
#             if((couldBeSame && nums[i] <= nums[r]) ||
#                (!couldBeSame && nums[i] < nums[r])) {
#                 swap(nums[p], nums[i]);
#                 ++p;
#             }
#         }
#         swap(nums[p], nums[r]);
#         if(p == k) {
#             return nums[p];
#         } else if(p < k) {
#             return quickSelect(p + 1, r, k, nums);
#         } else {
#             return quickSelect(l, p - 1, k, nums);
#         }
#     }
# public:
#     int findKthLargest(vector<int>& nums, int k) {
#         k = nums.size() - k;
#         return quickSelect(0, nums.size() - 1, k, nums);
#     }
# };
            
        
            
        