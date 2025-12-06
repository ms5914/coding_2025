class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def longestPalindromeSubseq(s: str) -> bool:
            n = len(s)
            dp = [[0] * n for _ in range(n)]

            for i in range(0, n):
                dp[i][i] = 1
            
            for i in range(0, n-1):
                j = i+1
                if s[i] == s[j]:
                    dp[i][j] = 2
                else:
                    dp[i][j] = 1
            
            for l in range(3, n+1):
                for i in range(0, n-l+1):
                    j = i+l-1
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            return not (len(s) - dp[0][n-1] > k)
        
        return longestPalindromeSubseq(s)
            