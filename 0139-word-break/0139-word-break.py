class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        class TrieNode:
            def __init__(self):
                self.children = dict()
                self.is_word = False
        
        root = TrieNode()
        for word in wordDict:
            curr = root
            for c in word:
                if not c in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True

        dp = [False]*len(s)
        for i in range(len(s)):
            if i == 0 or dp[i-1]:
                curr = root
                for j in range(i, len(s)):
                    if not s[j] in curr.children:
                        break
                    curr = curr.children[s[j]]
                    if curr.is_word:
                        dp[j] = True
        return dp[-1]
        

