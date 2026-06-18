class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = {}

        for ch in strs:
            x = tuple(sorted(ch))
            if x not in ans:
                ans[x] = [ch]
            else:
                ans[x].append(ch)
        return list(ans.values())
