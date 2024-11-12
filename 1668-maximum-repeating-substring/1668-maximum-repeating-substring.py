class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
#         initial_word = word
#         count = 0
#         while word in sequence:
#             count += 1
#             word += initial_word
            
#         return count
        n = len(sequence)
        m = len(word)
        
        dp = [0] * (n + 1)
        
        for i in range(m, n + 1):
            if sequence[i-m:i] == word:
                dp[i] = dp[i-m] + 1
            
        
        return max(dp)
            