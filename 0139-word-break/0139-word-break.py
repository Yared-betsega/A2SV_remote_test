class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         words = set(wordDict)
#         memo = {}
#         def dp(index):
#             if index == len(s):
#                 return True
#             if index in memo:
#                 return memo[index]
            
#             string = ""
#             for i in range(index, len(s)):
#                 string += s[i]
#                 if string in words:
#                     if dp(i + 1):
#                         memo[index] = True
#                         return True
#             memo[index] = False
#             return False
        
#         return dp(0)

        n = len(s)

        dp = [False] * (n+1)
        dp[n] = True


        for i in range(n-1, -1, -1):
          for w in wordDict:
            if (i + len(w)) <= n and s[i:i+len(w)] == w:
              dp[i] = dp[i+len(w)]
            if dp[i]:
              break

        return dp[0]

# time and space complexity
# time: O(n)
# space: O(n)
                    
                    
            