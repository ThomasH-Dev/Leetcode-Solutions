class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            skip = 1
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                skip +=1
            dfs(i + skip, cur, total)
        
        
        dfs(0, [],0)
        return res 