class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        for index, value in enumerate(indices):
            ans = ""
            for i in range(len(indices)):
                ans += s[indices.index(i)]
                
            return ans
        
        
        