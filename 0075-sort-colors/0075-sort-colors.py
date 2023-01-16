class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r = 0, len(nums)-1
        i = 0
        pivot = 1
        while i<=r:
            if nums[i] < pivot:
                nums[i], nums[l] = nums[l], nums[i]
                l +=1
            if nums[i] > pivot:
                nums[i],nums[r] = nums[r],nums[i]
                r-=1
                i -=1
            
            i +=1
            