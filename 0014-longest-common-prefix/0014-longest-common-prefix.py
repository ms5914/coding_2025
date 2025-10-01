class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs or len(strs)==0:
            return ""
        
        common_word = strs[0]
        n = len(common_word)
        for i in range(n):
            c = common_word[i]
            for word in strs[1:]:
                if i >= len(word) or word[i] !=c:
                    return common_word[:i]
        return common_word
        