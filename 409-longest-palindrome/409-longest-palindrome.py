class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        count = 0
        for i in range(len(s)):
                       
            if s[i] in seen:
                count +=2
                seen.remove(s[i])
            else:
                seen.add(s[i])
                
        
        if len(seen) > 0:
            count +=1 
        return count
                
            