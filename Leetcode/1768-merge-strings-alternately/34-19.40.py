class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word1 = list(word1)
        word2 = list(word2)
        result = []
        m = min(len(word1), len(word2))

        for i in range(m):
            result.append(word1[i])
            result.append(word2[i])
        return "".join(result) + ("".join(word1[i+1:]) if (len(word1) > len(word2)) else "".join(word2[i+1:]))

    
