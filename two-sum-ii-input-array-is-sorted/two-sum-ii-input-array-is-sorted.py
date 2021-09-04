class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index, value, in enumerate(numbers):
            
            remaining =  target-numbers[index]

            
            if remaining in seen:
                return [seen[remaining] +1, index+1]
            else:
                seen[value] =  index 