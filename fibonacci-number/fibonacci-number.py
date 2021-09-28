

class Solution:
   
    def fib(self, n: int, **dict ) -> int:
        d = {}
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in d:
            return d[n]
        else: 
            d[n] = self.fib(n-1) + self.fib(n-2)
        return d[n]
        
        
    
        