class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        result = []
        def find_combinations(index, curr_str_list):
            
            if index == len(digits):
                result.append("".join(curr_str_list))
                return
                
            for ch in mapp[int(digits[index])]:
                curr_str_list.append(ch)
                find_combinations(index+1, curr_str_list)
                curr_str_list.pop()
        
        find_combinations(0, [])
        return result
                
                
                
            
        
        
        