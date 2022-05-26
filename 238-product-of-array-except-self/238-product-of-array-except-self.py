class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        # get the first modified prefix
        for i in range(len(nums)):
            if i == 0:
                ans.append(1)
            else:
                ans.append(nums[i-1] * ans[i -1])
        # run through again calculating the modified postfix
        
        for i in range(len(nums)-1, -1,-1):
            if i != len(nums) -1:
                ans[i] = ans[i] * nums[i+1]
                nums[i] = nums[i+1]*nums[i]
        return ans
            
            