class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        nl = min(len(word1), len(word2))
        res = ""
        i = 0
        while i < nl:
            res = res + word1[i] + word2[i]
            i += 1
        
        if len(word1) > len(word2):
            res = res + word1[i:]
        elif len(word2) > len(word1):
            res = res + word2[i:]

        return res