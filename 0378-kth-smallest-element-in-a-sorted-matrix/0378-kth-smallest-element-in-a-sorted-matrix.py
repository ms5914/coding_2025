class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def find_smaller_and_equal(mid):
            i = len(matrix)-1
            j = 0
            count_smaller = 0
            smaller = matrix[0][0]
            larger = matrix[len(matrix)-1][len(matrix[0])-1]

            while i>=0 and j<len(matrix[0]):
                if matrix[i][j] <= mid:
                    count_smaller+=i+1
                    smaller = max(smaller, matrix[i][j])
                    j+=1
                else:
                    larger = min(larger, matrix[i][j])
                    i-=1
            return count_smaller, smaller, larger

        low = matrix[0][0]
        high = matrix[len(matrix)-1][len(matrix[0])-1]
        
        while low<high:
            mid = low+(high-low)//2
            count, smaller, larger = find_smaller_and_equal(mid)
            if count == k:
                return smaller
            elif count>k:
                high = smaller
            else:
                low = larger
        
        return low




