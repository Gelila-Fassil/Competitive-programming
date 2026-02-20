from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            signature = "".join(sorted(s))
            groups[signature].append(s)
        return list(groups.values())