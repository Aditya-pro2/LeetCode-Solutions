class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        num1, num2, num3 = 0, 0, 0
        for i in range(max(len(firstWord), len(secondWord), len(targetWord))):
            if i < len(firstWord):
                num1 = num1 * 10 + int(ord(firstWord[i]) - 97)
            if i < len(secondWord):
                num2 = num2 * 10 + int(ord(secondWord[i]) - 97)
            if i < len(targetWord):
                num3 = num3 * 10 + int(ord(targetWord[i]) - 97)
        return num1 + num2 == num3