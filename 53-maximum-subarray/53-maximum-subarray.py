class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = ans = nums[0]
        
        if len(nums) == 1:
            return nums[0]
        else:
            for i in range(1,len(nums)):
                if nums[i-1] > 0:
                    nums[i] = nums[i] + nums[i - 1]
                count = nums[i]
                ans = max(count, ans)
            print(nums)
            return ans
                