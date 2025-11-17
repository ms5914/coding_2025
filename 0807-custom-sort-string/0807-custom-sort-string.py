class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count_letters = Counter(s)
        result_str = []
        for ch in order:
            if ch in count_letters:
                for i in range(count_letters[ch]):   
                    result_str.append(ch)
                del count_letters[ch]
        
        for ch in count_letters:
            for i in range(count_letters[ch]):
                result_str.append(ch)
        
        return "".join(result_str)



        