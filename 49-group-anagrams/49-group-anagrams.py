class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            d[sortedWord] = d.get(sortedWord, []) + [word]
        return d.values()