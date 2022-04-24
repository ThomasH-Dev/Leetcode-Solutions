class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for i, word in enumerate(strs):
            key = tuple(sorted(word))
            d[key] = d.get(key, []) + [word]
        return d.values()