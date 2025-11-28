class Solution:
    def maxOperations(self, s: str) -> int:
        
        zero_groups_so_far = 0
        total_operations = 0
        ones_so_far = 0
        i=0
        while i<len(s):
            
            if s[i] == "0":
                while i<len(s) and s[i] == "0":
                    i+=1
                total_operations+=ones_so_far
            else:
                ones_so_far+=1
                i+=1
        
        return total_operations

            

            

        