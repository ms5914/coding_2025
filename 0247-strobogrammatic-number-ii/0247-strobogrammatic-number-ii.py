class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # Helper function to build recursively
        def helper(k):
            # Base Case: odd length (middle digit)
            if k == 0: return [""]
            if k == 1: return ["0", "1", "8"]
            
            # Recursive step: get list of size k-2
            prev_list = helper(k - 2)
            result = []
            
            pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
            
            for s in prev_list:
                for pair in pairs:
                    # Special case: We cannot put '0' at the start (outermost layer)
                    # unless n was originally 1 (handled in base case k=1)
                    if pair[0] == '0' and k == n:
                        continue
                    
                    result.append(pair[0] + s + pair[1])
            
            return result

        return helper(n)