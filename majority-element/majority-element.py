class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority = nums[0]
        count = 1
        print(majority)
        for i in range(1,len(nums)):
            if nums[i] == majority:
                count += 1
                print("count after addition", count )
            else:
                count -= 1
                print("count after sub", count )
                if count == 0 and i < len(nums):
                    majority = nums[i+1]
                    print(majority)
                    
        return majority 