class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate = "".join(c.lower() for c in licensePlate if c.isalpha())
        words = sorted(words, key=len)
        for word in words:
            for i in range(len(licensePlate)):
                if word.count(licensePlate[i]) < licensePlate.count(licensePlate[i]):
                    break
                if i == len(licensePlate) - 1:
                    return word