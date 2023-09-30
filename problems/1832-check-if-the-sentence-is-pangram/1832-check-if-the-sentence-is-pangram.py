class Solution:
    def checkIfPangram(self, s: str) -> bool:
        for i in range(1, 27):
            if chr(i + 96) not in s:
                return False
        return True