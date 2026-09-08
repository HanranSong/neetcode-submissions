class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            word = strs[i]
            common_len = 0
            while (
                common_len < len(prefix)
                and common_len < len(word)
                and prefix[common_len] == word[common_len]
            ):
                common_len += 1
            prefix = prefix[:common_len]
            if not prefix:
                return ""
        return prefix
