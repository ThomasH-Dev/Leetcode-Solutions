class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            for i in range(1, len(nums)):
                nums[i] = max( nums[i-1] + nums[i], nums[i] )
            print(nums)
            return max(nums)