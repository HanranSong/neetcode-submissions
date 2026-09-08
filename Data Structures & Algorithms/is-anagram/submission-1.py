class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        base = ord("a")
        for i, j in zip(s, t):
            count[ord(i) - base] += 1
            count[ord(j) - base] -= 1
        return not any(count)