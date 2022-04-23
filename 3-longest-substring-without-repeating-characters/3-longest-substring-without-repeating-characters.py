class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = maxCount = 0
        for index, character in enumerate(s):
            # we must re-adjust start to keep accurate count
            if character in seen and seen[character] >= start:
                start = seen[character] + 1
                print(start)
            
            
            else:
                maxCount = max(maxCount, (index - start) + 1)
            seen[character] = index
        return maxCount
                
                