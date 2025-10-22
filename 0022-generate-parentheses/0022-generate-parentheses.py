class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def create_combinations(open_count, closed_count, result_str_list):
            
            if open_count == n and closed_count == n:
                result.append("".join(result_str_list))
                return
            elif open_count > n or closed_count > n:
                return
            
            else:
                if open_count == closed_count:
                    result_str_list.append("(")
                    create_combinations(open_count+1, closed_count, result_str_list)
                    result_str_list.pop()
                    
                else:
                    result_str_list.append(")")
                    create_combinations(open_count, closed_count+1, result_str_list )
                    result_str_list.pop()
                    
                    result_str_list.append("(")
                    create_combinations(open_count+1, closed_count, result_str_list)
                    result_str_list.pop()
                    
                    
        create_combinations(0, 0, [])
        return result
                    
                    
                    
                
        