class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        tuples = []
        ans = []
        for i in range(len(strs)):
            x = sorted(tuple(strs[i]))
            tuples.append(x)
        for i in range(len(tuples)):
            d[tuple(tuples[i])] = []
        for i in range(len(tuples)):
            d[tuple(tuples[i])].append(strs[i])
        for key in d:
            ans.append(d[key])
        return ans
