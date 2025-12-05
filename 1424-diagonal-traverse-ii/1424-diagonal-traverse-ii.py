class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        ans = []
        dq = deque()
        dq.append((0, 0))
        # ans.append(nums[0][0])
        while dq:
            row, col = dq.popleft()
            ans.append(nums[row][col])
            if col == 0 and row+1<len(nums):
                dq.append((row+1, col))
            if col+1 < len(nums[row]):
                dq.append((row, col+1))
                
        
        return ans
            
            
            

        # min_diagonal = float("inf")
        # max_diagonal = -float("inf")

        # diagonal_dict = defaultdict(list)
        # for row in range(len(nums)-1, -1, -1):
        #     for col in range(len(nums[row])):
        #         diagonal = row+col
        #         min_diagonal = min(diagonal, min_diagonal)
        #         max_diagonal = max(diagonal, max_diagonal)
        #         diagonal_dict[diagonal].append(nums[row][col])
        

        # ans = []
        # for diag in range(min_diagonal, max_diagonal+1, 1):
        #     if diag in diagonal_dict:
        #         for ele in diagonal_dict[diag]:
        #             ans.append(ele)
        
        # return ans


                

        