class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if len(s) == 1:
            return True
        else: 
            res = self.helper(s)
            if res == False:
                return False
        return True
    def helper(self, s):
        mid = len(s) /2 
        for i in range(len(s)):
            if i == mid and len(s) % 2 == 1:
                break
            elif s[i] != s[len(s)-1-i]:
                return False
                
    
                   
                    
            
                
        