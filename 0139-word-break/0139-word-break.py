class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)

        self.nested_substring(s)
        string = s
        @lru_cache(maxsize=None)
        def can_break(start):
            if start == len(string):
                return True
            for end in range(start+1, len(string)+1):
                prefix = self.nested.get((start, end), None)
                if prefix in word_set:
                    if can_break(end):
                        return True 
            return False
        return can_break(0)

    
    def nested_substring(self, word):
        self.nested = dict()
        for i in range(0, len(word)):
            for j in range(i+1, len(word)+1):
                self.nested[(i,j)] = word[i:j]
        