class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] +=1
            else:
                d[nums[i]] = 1
        sorted_d = sorted(d.items(), key = lambda x: x[1],reverse = True)
        print(sorted_d)
        for i in range(k):
            ans.append(sorted_d[i][0])
        return ans
            