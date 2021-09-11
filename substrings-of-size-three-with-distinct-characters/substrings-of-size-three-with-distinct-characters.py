class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        dict = {}
        count = 0
        for i, value in enumerate(s):
            dict[i] = value
        
        for i in range(len(s)-2):
            if dict[i] != dict[i+1] and dict[i] != dict[i + 2] and dict[i+1] != dict[i + 2]:
                print(dict[i], dict[i+1],dict[i+2])
                count +=1
                print(count)
            else: 
                print("repeated")
        return count 