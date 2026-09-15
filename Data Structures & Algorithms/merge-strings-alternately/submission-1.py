from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        for a, b in zip_longest(word1, word2): 
            if a is not None:
                merged += a
            if b is not None:
                merged += b
        return merged
        
