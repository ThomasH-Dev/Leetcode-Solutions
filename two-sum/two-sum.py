class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value, in enumerate(nums):
            
            remaining = target - nums[index]
            
            if remaining in seen:
                return [index,seen[remaining]]
            else:
                seen[value]=index
                