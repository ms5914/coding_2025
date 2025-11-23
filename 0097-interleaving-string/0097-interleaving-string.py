class Solution:

    @lru_cache(maxsize = None)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if not s1 and not s2 and not s3:
            return True
        ptr1, ptr2, ptr3 = 0, 0, 0
        while ptr1 < len(s1) and ptr3<len(s3) and s1[ptr1] == s3[ptr3]:
            ptr1+=1
            ptr3+=1
            if self.isInterleave(s1[ptr1:], s2, s3[ptr3:]):
                return True
        
        ptr1, ptr2, ptr3 = 0, 0, 0
        while ptr2 < len(s2) and ptr3<len(s3) and s2[ptr2] == s3[ptr3]:
            ptr2+=1
            ptr3+=1
            if self.isInterleave(s1, s2[ptr2:], s3[ptr3:]):
                return True
        return False
        
        



            
            
        
        