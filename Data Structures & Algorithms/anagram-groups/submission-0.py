class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        base = ord("a")
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - base] += 1
            key = tuple(count)
            groups.setdefault(key, []).append(word)
        return list(groups.values())