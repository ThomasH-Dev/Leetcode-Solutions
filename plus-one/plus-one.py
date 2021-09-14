class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:    
        s = ""
        for i, value in enumerate(digits):
            s += str(value)
        s=str(int(s)+1) 
        arr = list(s)
        
        return arr