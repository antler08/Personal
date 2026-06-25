class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = []
        m = min(len(word1), len(word2))

        for i in range(m):
            result.append(word1[i])
            result.append(word2[i])

        return "".join(result) + word1[m:] + word2[m:]