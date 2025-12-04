class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = []
        max_count = 0
        char_set = set()


        def find_max(i, char_set, char_count, indexes):  
            nonlocal max_count     
            if char_count>max_count:
                max_count = char_count
                result = list(indexes)
            if i>=len(arr):
                return
            
            found = False
            word_set = set()
            for ch in arr[i]:
                if ch in char_set or ch in word_set:
                    found = True
                    break
                word_set.add(ch)
            if not found:
                for ch in arr[i]:
                    char_set.add(ch)
                indexes.add(i)
                find_max(i+1,char_set, char_count+len(arr[i]), indexes)
                for ch in arr[i]:
                    if ch in char_set:
                        char_set.remove(ch)
                indexes.remove(i)
            find_max(i+1, char_set, char_count, indexes)
        
        find_max(0, set(), 0, set())
        return max_count
            

            


        