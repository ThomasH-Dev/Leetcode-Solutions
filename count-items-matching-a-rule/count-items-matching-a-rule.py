class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dict = {"type":0,"color":1,"name": 2}
        keyIndex = dict[ruleKey]
        count = 0
        for i, value in enumerate(items):
            if value[keyIndex] == ruleValue:
                count +=1
        return count