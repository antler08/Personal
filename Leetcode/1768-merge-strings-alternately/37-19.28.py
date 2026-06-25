class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word1 = list(word1)
        word2 = list(word2)
        result = []

        for i in range((len(word1) if (len(word1) < len(word2)) else len(word2))):
            result.append(word1.pop(0))
            result.append(word2.pop(0))

        
        return "".join(result) + str("".join(word1) if (len(word1) > len(word2)) else "".join(word2))