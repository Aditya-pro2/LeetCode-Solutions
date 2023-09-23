class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        c, n = 0, len(words)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if words[i] == words[j][::-1]:
                    c += 1
        return c