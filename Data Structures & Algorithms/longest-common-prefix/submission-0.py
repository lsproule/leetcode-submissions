def trim(prefix, other):
    while prefix != other[:len(prefix)] and prefix != "":
        print(f"{prefix = } {other[:len(prefix)] = }")
        prefix = prefix[:-1]
        print(f"{prefix = } {other[:len(prefix)] = }")
    return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            prefix = trim(prefix, word)
        return prefix 