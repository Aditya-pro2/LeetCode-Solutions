class Solution:
    def isThree(self, n: int) -> bool:
        l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        x = sqrt(n)
        if int(x) == x and x in l:
            return True
        return False