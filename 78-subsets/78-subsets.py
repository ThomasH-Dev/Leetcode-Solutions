class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset= []
        def dfs(i):
            
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            skp = 1
            while i +1  < len(nums) and nums[i+1] == nums[i]:
                skp +=1
                
            
            dfs(i + skp)
            
        dfs(0)
        return res