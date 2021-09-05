class Solution:
    def isHappy(self, n: int) -> bool:
        curr = 0 
        s = set()
        while n != 1:
            n = sum([int(i)**2 for i in str(n)])
            if n in s:
                return False
            else:
                
                s.add(n)
        return True
            
            