class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels_count = 0
        right = 0
        while right < k - 1:
            if s[right] in vowels:
                vowels_count += 1
            right += 1
        
        left = result = 0
        while right < len(s):
            if s[right] in vowels:
                vowels_count += 1
                
            result = max(vowels_count, result)
            
            if s[left] in vowels:
                vowels_count -= 1
            left += 1
            right += 1
        
        return result
            
        